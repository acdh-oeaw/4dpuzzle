from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist
from django.db.models.query import QuerySet

from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF


from browsing.browsing_utils import model_to_dict


ARCHE_BASE_URI = getattr(settings, 'ARCHE_BASE_URI', 'https://id.acdh.oeaw.ac.at/MYPROJECT')


repo_schema = "https://raw.githubusercontent.com/acdh-oeaw/repo-schema/master/acdh-schema.owl"
acdh_ns = Namespace("https://vocabs.acdh.oeaw.ac.at/acdh#")
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


def get_arche_id(res, id_prop="pk", arche_uri="https://id.acdh.oeaw.ac.at"):
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


def as_arche_res(res, res_type='Resource'):
    g = Graph()
    sub = URIRef(get_arche_id(res))
    g.add( (sub, RDF.type, acdh_ns[res_type]))

    for x in get_arche_fields(res):
        cur_val = x['value']
        arche_prop = x['extra_fields']['arche_prop'].strip()
        arche_prop_domain = ARCHE_PROPS_LOOKUP.get(arche_prop,'No Match')
        if arche_prop_domain == 'string':
            g.add( (sub, acdh_ns[arche_prop], Literal(cur_val)) )
        elif arche_prop_domain == 'date':
            g.add( (sub, acdh_ns[arche_prop], Literal(cur_val, datatype=XSD.date)) )
        else:
            if isinstance(cur_val, QuerySet):
                for obj in cur_val:
                    if obj is not None:
                        g.add( (sub, acdh_ns[arche_prop], URIRef(get_arche_id(obj))) )
            else:
                if cur_val is not None:
                    g.add( (sub, acdh_ns[arche_prop], URIRef(get_arche_id(cur_val))) )
    return g


def qs_as_arche_res(qs, res_type='Resource'):
    maingraph = Graph()
    for res in qs:
        try:
            maingraph += as_arche_res(res, res_type=res_type)
        except Exception as e:
            print(res, e)
    return maingraph
