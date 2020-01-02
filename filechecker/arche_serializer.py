from rdflib import Graph, Namespace, URIRef, Literal, XSD
from rdflib.namespace import RDF

from archeutils.utils import as_arche_res


def fc_col_as_arche(res):
    return as_arche_res(res, res_type='Collection', arche_prop='fc_arche_id')
