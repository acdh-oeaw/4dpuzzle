from django.conf.urls import include, url
from django.contrib import admin
from . import api_views

urlpatterns = [
    url(r'^brickgeojson/(?P<pk>[0-9]+)$', api_views.brick_geojson, name='brickgeojson'),
    url(r'^bricksgeojson/$', api_views.bricks_geojson, name='bricksgeojson'),
    url(r'^findsgeojson/$', api_views.finds_geojson, name='findsgeojson'),
    url(r'^findgeojson/(?P<pk>[0-9]+)$', api_views.find_geojson, name='findgeojson'),
    url(
        r'^stratunitsgeojson/$',
        api_views.stratunits_geojson, name='stratunitsgeojson'
    ),
    url(r'^stratunitgeojson/(?P<pk>[0-9]+)$', api_views.stratunit_geojson, name='stratunitgeojson'),
    url(
        r'^excavationobjects/$',
        api_views.excavationobjects_geojson, name='excavationobjects'
    ),
    url(
        r'^excavationobject/(?P<pk>[0-9]+)$',
        api_views.excavationobject_geojson, name='excavationobject'
    ),
    url(
        r'^terrains/$',
        api_views.terrains_geojson, name='terrainsgeojson'
    ),
    url(
        r'^terrain/(?P<pk>[0-9]+)$',
        api_views.terrain_geojson, name='terraingeojson'
    ),
    url(
        r'^trenchs/$',
        api_views.trenchs_geojson, name='trenchsgeojson'
    ),
    url(
        r'^trench/(?P<pk>[0-9]+)$',
        api_views.trench_geojson, name='trenchgeojson'
    ),

]
