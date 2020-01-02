from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF

from archeutils.utils import (
    ARCHE_PROPS_LOOKUP, ARCHE_LANG, ARCHE_CONST_MAPPINGS, acdh_ns
)


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
    else:
        g.add((sub, RDF.type, acdh_ns.Collection))
        if res.parent:
            g.add((sub, acdh_ns.isPartOf, URIRef(res.parent.fc_arche_id)))
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
    return g
