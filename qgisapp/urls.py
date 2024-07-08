from django.urls import path
from . import views

app_name = "qgisapp"
urlpatterns = [
    path("map/", views.QgisMapView.as_view(), name="qgis_map"),
]
