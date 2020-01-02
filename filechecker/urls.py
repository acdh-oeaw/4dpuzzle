from django.urls import include, path
from . import views

app_name = "filechecker"

urlpatterns = [
    path('<model_name>/<pk>', views.res_as_arche_graph, name='res_as_arche_graph'),
    path('<model_name>', views.qs_as_arche_graph, name='qs_as_arche_graph'),
    # path('cached/<app_name>/<model_name>', views.cashed_graph_data, name='cached_graph'),
    # path('preview/<app_name>/<model_name>', views.preview_graph_data, name='preview_graph'),
    # path('<app_name>/<model_name>', views.CachednetvisView.as_view(), name='cached_graph_html'),
]
