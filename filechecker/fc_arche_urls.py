from django.urls import include, path
from . import arche_views

app_name = "filechecker"

urlpatterns = [
    path(
        "collection-and-resources/<pk>",
        arche_views.children_as_arche_graph,
        name="collection_and_resources_as_graph",
    ),
    path(
        "<model_name>/<pk>", arche_views.res_as_arche_graph, name="res_as_arche_graph"
    ),
    path("<model_name>", arche_views.qs_as_arche_graph, name="qs_as_arche_graph"),
]
