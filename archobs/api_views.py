from django.http import HttpResponse
from django.core.serializers import serialize
from .models import *


def trenchs_geojson(request):
    trenchs_as_geojson = serialize('geojson', Trench.objects.all())
    return HttpResponse(trenchs_as_geojson, content_type='json')


def trench_geojson(request, pk):
    trench_as_geojson = serialize('geojson', Trench.objects.filter(id=pk))
    return HttpResponse(trench_as_geojson, content_type='json')


def terrains_geojson(request):
    terrains_as_geojson = serialize('geojson', Terrain.objects.all())
    return HttpResponse(terrains_as_geojson, content_type='json')


def terrain_geojson(request, pk):
    terrain_as_geojson = serialize('geojson', Terrain.objects.filter(id=pk))
    return HttpResponse(terrain_as_geojson, content_type='json')


def excavationobjects_geojson(request):
    excavationobjects_as_geojson = serialize('geojson', ExcavationObject.objects.all())
    return HttpResponse(excavationobjects_as_geojson, content_type='json')


def excavationobject_geojson(request, pk):
    excavationobject_as_geojson = serialize('geojson', ExcavationObject.objects.filter(id=pk))
    return HttpResponse(excavationobject_as_geojson, content_type='json')


def stratunits_geojson(request):
    stratunits_as_geojson = serialize('geojson', Stratunit.objects.all())
    return HttpResponse(stratunits_as_geojson, content_type='json')


def finds_geojson(request):
    finds_as_geojson = serialize('geojson', Find.objects.all())
    return HttpResponse(finds_as_geojson, content_type='json')


def bricks_geojson(request):
    bricks_as_geojson = serialize('geojson', Brick.objects.all())
    return HttpResponse(bricks_as_geojson, content_type='json')


def brick_geojson(request, pk):
    bricks_as_geojson = serialize('geojson', Brick.objects.filter(id=pk))
    return HttpResponse(bricks_as_geojson, content_type='json')


def find_geojson(request, pk):
    finds_as_geojson = serialize('geojson', Find.objects.filter(id=pk))
    return HttpResponse(finds_as_geojson, content_type='json')


def stratunit_geojson(request, pk):
    stratunit_as_geojson = serialize('geojson', Stratunit.objects.filter(id=pk))
    return HttpResponse(stratunit_as_geojson, content_type='json')
