from django.urls import include, path
from . import arche_rdf_views

app_name = "archeutils"

urlpatterns = [
    path('4arche/<app_name>', arche_rdf_views.relevante_classes, name='resolve_id_to_graph'),
    path('resolve', arche_rdf_views.resolve_id_to_graph, name='resolve_id_to_graph'),
    path(
        'fbd/<app_name>/<model_name>',
        arche_rdf_views.fbd_arche_rdf,
        name='fbd_arche_rdf'
    ),
    path(
        '<app_name>/<model_name>/<pk>',
        arche_rdf_views.res_as_arche_graph,
        name='res_as_arche_graph'
    ),
    path('<app_name>/<model_name>', arche_rdf_views.qs_as_arche_graph, name='qs_as_arche_graph'),
]
