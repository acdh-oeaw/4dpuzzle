import pickle
import os
import re


from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from django.db.models.query import QuerySet

from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF

from browsing.browsing_utils import model_to_dict

from . configs import EXTENSION_HAS_CATEGORY_MAPPING

ARCHE_CONST_MAPPINGS = getattr(settings, 'ARCHE_CONST_MAPPINGS', False)

ARCHE_LANG = getattr(settings, 'ARCHE_LANG', 'en')
ARCHE_BASE_URI = getattr(settings, 'ARCHE_BASE_URI', 'https://id.acdh.oeaw.ac.at/MYPROJECT')
ARCHE_PREFIX_REMOVE = getattr(settings, 'ARCHE_PREFIX_REMOVE', '')

pickle_file = os.path.join(settings.BASE_DIR, 'archeutils', 'arche_descriptions.pickle')

ARCHE_RE_PATTERN = re.compile(r'{(.*?)}', re.IGNORECASE)
# regex = re.compile(ARCHE_RE_PATTERN, re.IGNORECASE)

with open(pickle_file, "rb") as input_file:
    ARCHE_DESC_DICT = pickle.load(input_file)


repo_schema = "https://raw.githubusercontent.com/acdh-oeaw/repo-schema/master/acdh-schema.owl"
acdh_ns = Namespace("https://vocabs.acdh.oeaw.ac.at/schema#")
owl_ns = Namespace("http://www.w3.org/2002/07/owl#")
rdfs_ns = Namespace("http://www.w3.org/2000/01/rdf-schema#")


def get_prop_types(repo_schema_url=repo_schema):
    g = Graph()
    g.parse(repo_schema, format='xml')
    prop_types = {}
    for s in g.subjects(RDF.type, None):
        if s.startswith('https://vocabs.acdh'):
            prop_name = s.split('#')[-1]
            for range_prop in g.objects(s, rdfs_ns.range):
                prop_types[prop_name] = range_prop.split('#')[-1]
    return prop_types


ARCHE_PROPS_LOOKUP = get_prop_types()


def get_arche_desc(res):
    class_name = res.__class__.__name__.lower()
    desc_dict = ARCHE_DESC_DICT.get(class_name, None)
    if desc_dict is not None:
        lookup_dict = {}
        for x in set(re.findall(ARCHE_RE_PATTERN, desc_dict)):
            value = str(getattr(res, x, f"no property {x} defined"))
            if value == 'None' or value.endswith('None'):
                value = f"no value provided for property {x}"
            else:
                pass
            lookup_dict[x] = f"'{value}'"
        desc = desc_dict.format(**lookup_dict)
        return desc
    else:
        "No description template found"


def directory_to_col_id(
    res, path_prop='fc_directory', pre_remove=ARCHE_PREFIX_REMOVE, pre_add=ARCHE_BASE_URI
):
    """ creates a col-id from a file path
        :param path_prop: The resource' property providing the binary location path
        :pre_remove: some prefix which should be replaced
        :pre_add: The projects base URI
        :return: An arche id of the acdh:partOf collection
    """
    orig_path = getattr(res, path_prop)
    if orig_path is not None:
        new_path = orig_path.replace(pre_remove, f"{pre_add}/")
    else:
        new_path = None
    return new_path


def get_p4d_id(res, arche_uri=ARCHE_BASE_URI, arche_prop=False):
    """ function to generate a the canonical p4d ID
        :param res: A model object
        :param arche_uri: A base url; should be configued in the projects settings file
        :return: An canonical ARCHE-ID (URI)

    """
    if arche_prop:
        return getattr(res, arche_prop)
    elif res.fc_filename and res.fc_directory:
        new_path = directory_to_col_id(res)
        if new_path.endswith('/'):
            return f"{new_path}{res.fc_filename}"
        else:
            return f"{new_path}/{res.fc_filename}"


def get_category(
    res,
    prop="fc_extension",
    mapping=EXTENSION_HAS_CATEGORY_MAPPING,
    default='https://vocabs.acdh.oeaw.ac.at/archecategory/dataset'
):
    """ maps an object to an acdh:hasCategory value by an object's property
        :param res: A django model object
        :param prop: The property providing a file extension, defaults to "fc_extension"
        :param mapping: a dict mapping the file extension to a category
        :param default: a default cateogry in case no match for the provided mapping
        :return: A string with the URL of the matching category
    """
    category = default
    extension = getattr(res, prop)
    if extension is not None:
        category = mapping.get(extension.lower().strip(), default)
    return category


def get_arche_id(res, id_prop="pk", arche_uri=ARCHE_BASE_URI):
    """ function to generate generic ARCHE-IDs
        :param res: A model object
        :param id_prop: The object's primary key property
        :param arche_uri: A base url; should be configued in the projects settings file
        :return: An ARCHE-ID (URI)

    """
    app_name = res.__class__._meta.app_label.lower()
    class_name = res.__class__.__name__.lower()
    return "/".join(
        [arche_uri, app_name, class_name, f"{getattr(res, id_prop)}"]
    )


def get_arche_fields(
    res, extra_fields_name='extra_fields', arche_prop_name='arche_prop'
):
    vals = [x for x in model_to_dict(res) if x.get('value') != '']
    vals = [x for x in vals if x.get('value') != 'None']
    vals = [x for x in vals if x.get('value') is not None]
    vals = [x for x in vals if x.get(extra_fields_name)]
    vals = [x for x in vals if x.get(extra_fields_name).get(arche_prop_name)]
    return vals


def col_id_from_res(res, arche_uri=ARCHE_BASE_URI):
    col_name = res.__class__.__name__.lower()
    return "/".join([arche_uri, col_name])


def col_from_res(res, arche_uri=ARCHE_BASE_URI):
    g = Graph()
    sub = URIRef(directory_to_col_id(res))
    g.add((sub, RDF.type, acdh_ns.Collection))
    g.add((sub, acdh_ns.hasDescription, Literal(res.__class__.__doc__, lang=ARCHE_LANG)))
    g.add((sub, acdh_ns.hasIdentifier, URIRef(col_id_from_res(res))))
    for const in ARCHE_CONST_MAPPINGS:
        g.add((sub, acdh_ns[const[0]], URIRef(const[1])))
    return g


def as_arche_res(res, res_type='Resource', arche_prop=False):
    g = Graph()
    sub = URIRef(get_arche_id(res,))
    g.add((sub, RDF.type, acdh_ns[res_type]))
    g.add((sub, acdh_ns.hasIdentifier, URIRef(get_p4d_id(res, arche_prop=arche_prop))))
    g.add((
        sub, acdh_ns.hasDescription, Literal(get_arche_desc(res), lang=ARCHE_LANG)
    ))
    # g.add((sub, acdh_ns.isPartOf, URIRef(directory_to_col_id(res))))
    if res_type == 'Collection':
        pass
    else:
        g.add((sub, acdh_ns.hasCategory, URIRef(get_category(res))))
    for x in get_arche_fields(res):
        cur_val = x['value']
        arche_prop = x['extra_fields']['arche_prop'].strip()
        arche_prop_domain = ARCHE_PROPS_LOOKUP.get(arche_prop, 'No Match')
        if arche_prop_domain == 'string':
            g.add((sub, acdh_ns[arche_prop], Literal(cur_val, lang=ARCHE_LANG)))
        elif arche_prop_domain == 'date':
            g.add((sub, acdh_ns[arche_prop], Literal(cur_val, datatype=XSD.date)))
        else:
            if isinstance(cur_val, QuerySet):
                for obj in cur_val:
                    if obj is not None:
                        g.add((sub, acdh_ns[arche_prop], URIRef(get_arche_id(obj))))
            else:
                if cur_val is not None:
                    g.add((sub, acdh_ns[arche_prop], URIRef(get_arche_id(cur_val))))
        for const in ARCHE_CONST_MAPPINGS:
            arche_prop_domain = ARCHE_PROPS_LOOKUP.get(const[0], 'No Match')
            print(arche_prop_domain)
            if arche_prop_domain == 'date':
                g.add((sub, acdh_ns[const[0]], Literal(const[1], datatype=XSD.date)))
            else:
                g.add((sub, acdh_ns[const[0]], URIRef(const[1])))
    return g


def qs_as_arche_res(qs, res_type='Resource'):
    maingraph = Graph()
    for res in qs:
        try:
            maingraph += as_arche_res(res, res_type=res_type)
        except Exception as e:
            print(res, e)
    return maingraph
