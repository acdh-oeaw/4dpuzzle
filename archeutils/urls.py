from django.urls import include, path
from . import arche_rdf_views

app_name = "archeutils"

urlpatterns = [
    path('<app_name>/<model_name>/<pk>', arche_rdf_views.res_as_arche_graph, name='res_as_arche_graph'),
    path('<app_name>/<model_name>', arche_rdf_views.qs_as_arche_graph, name='qs_as_arche_graph'),
]
