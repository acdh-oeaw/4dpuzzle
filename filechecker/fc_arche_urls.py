from django.urls import include, path
from . import arche_views

app_name = "filechecker"

urlpatterns = [
    path('<model_name>/<pk>', arche_views.res_as_arche_graph, name='res_as_arche_graph'),
    path('<model_name>', arche_views.qs_as_arche_graph, name='qs_as_arche_graph'),
]
