from django.conf.urls import url
from . import views

app_name = 'qgisapp'
urlpatterns = [
    url(
        r'^map/$',
        views.QgisMapView.as_view(),
        name='qgis_map'
    ),
]
