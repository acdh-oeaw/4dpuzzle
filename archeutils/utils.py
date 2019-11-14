from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, FieldDoesNotExist

from rdflib import Graph, Namespace
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


def get_arche_fields(res):
    vals = [x for x in model_to_dict(res) if x.get('value') != '']
    vals = [x for x in vals if x.get('value') != 'None']
    vals = [x for x in vals if x.get('extra_fields')]
    vals = [x for x in vals if x.get('extra_fields').get('arche_prop')]
    return vals


def get_field_extra(obj, field_name, extra='arche_prop'):
    try:
        my_field = obj._meta.get_field(field_name)
    except FieldDoesNotExist:
        return False
    try:
        extra_dict = my_field.extra
    except AttributeError:
        return False
    return extra_dict.get(extra, 'False')


g = Graph()
sub = URIRef(get_arche_id(res))
g.add( (sub, RDF.type, acdh_ns.Resource))

for x in get_arche_fields(res):
    cur_val = x['value']
    arche_prop = x['extra_fields']['arche_prop'].strip()
    arche_prop_domain = ARCHE_PROPS_LOOKUP.get(arche_prop,'No Match')
    if arche_prop_domain == 'string':
        g.add( (sub, acdh_ns[arche_prop], Literal(cur_val)) )
    elif arche_prop_domain == 'date':
        g.add( (sub, acdh_ns[arche_prop], Literal(cur_val)) )
    else:
        if isinstance(cur_val, QuerySet):
            for obj in cur_val:
                g.add( (sub, acdh_ns[arche_prop], URIRef(get_arche_id(obj))) )
        else:
            g.add( (sub, acdh_ns[arche_prop], URIRef(get_arche_id(cur_val))) )
