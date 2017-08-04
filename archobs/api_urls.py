from django.conf.urls import include, url
from django.contrib import admin
from . import api_views

urlpatterns = [
    url(r'^brickgeojson/(?P<pk>[0-9]+)$', api_views.brick_geojson, name='single_brick'),
    url(r'^bricksgeojson/', api_views.bricks_geojson, name='bricksgeojson'),
    url(r'^findsgeojson/', api_views.finds_geojson, name='findsgeojson'),
    url(r'^stratunitsgeojson/', api_views.stratunits_geojson, name='stratunitsgeojson'),
]
