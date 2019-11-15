from django.urls import include, path
from . import views

app_name = "archeutils"

urlpatterns = [
    path('<app_name>/<model_name>/<pk>', views.as_arche_graph, name='as_arche_graph'),
    # path('graph/<app_name>/<model_name>', views.qs_graph_data, name='qs_as_graph'),
    # path('cached/<app_name>/<model_name>', views.cashed_graph_data, name='cached_graph'),
    # path('preview/<app_name>/<model_name>', views.preview_graph_data, name='preview_graph'),
    # path('<app_name>/<model_name>', views.CachednetvisView.as_view(), name='cached_graph_html'),
]
