from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF

from archeutils.utils import (
    ARCHE_PROPS_LOOKUP,
    ARCHE_LANG,
    ARCHE_CONST_MAPPINGS,
    ARCHE_BASE_URI,
    acdh_ns,
    get_category
)


def fetch_access_restriction(res):
    access_res = None
    if res.fc_arche_access:
        access_res = res.fc_arche_access
        return access_res
    elif getattr(res, 'fc_directory', False):
        access_res = res.fc_directory.fc_arche_access
        if len(access_res) > 0:
            return access_res
        else:
            return None
    else:
        return access_res


def get_arche_fields(res):
    fields = []
    for x in res._meta._get_fields():
        if getattr(x, 'extra', False) and getattr(res, x.name, False):
            value = getattr(res, x.name, False)
            datatype = ARCHE_PROPS_LOOKUP.get(x.extra['arche_prop'])
            fields.append(
                {
                    "arche_prop": x.extra['arche_prop'],
                    "cur_val": f"{getattr(res, x.name)}",
                    "arche_prop_domain": datatype
                }
            )
    return fields


def as_arche_graph(res):
    g = Graph()
    sub = URIRef((res.fc_arche_id))
    if res.__class__._meta.model_name.lower() == 'fcresource':
        g.add((sub, RDF.type, acdh_ns.Resource))
        g.add((sub, acdh_ns.isPartOf, URIRef(res.fc_directory.fc_arche_id)))
        g.add((sub, acdh_ns.hasCategory, URIRef(get_category(res, prop='fc_extension'))))
    else:
        g.add((sub, RDF.type, acdh_ns.Collection))
        if res.parent:
            g.add((sub, acdh_ns.isPartOf, URIRef(res.parent.fc_arche_id)))
        else:
            g.add((sub, acdh_ns.isPartOf, URIRef(ARCHE_BASE_URI)))
    access_res = fetch_access_restriction(res)
    if access_res:
        g.add((sub, acdh_ns.hasAccessRestriction, URIRef(access_res)))
    for const in ARCHE_CONST_MAPPINGS:
        g.add((sub, acdh_ns[const[0]], URIRef(const[1])))
    for x in get_arche_fields(res):
        cur_val = x['cur_val']
        arche_prop = x['arche_prop']
        arche_prop_domain = x['arche_prop_domain']
        if arche_prop_domain == 'string':
            g.add((sub, acdh_ns[arche_prop], Literal(cur_val, lang=ARCHE_LANG)))
        elif arche_prop_domain == 'date':
            g.add((sub, acdh_ns[arche_prop], Literal(cur_val, datatype=XSD.date)))
        else:
            g.add((sub, acdh_ns[arche_prop], URIRef(cur_val)))
    if res.fc_custom_rdf:
        custom_graph = Graph()
        try:
            custom_graph.parse(data=res.fc_custom_rdf, format='n3')
        except Exception as e:
            print(e)
            return g
        return custom_graph + g
    else:
        return g


def qs_as_arche_res(qs):
    maingraph = Graph()
    for res in qs:
        maingraph += as_arche_graph(res)
    return maingraph
