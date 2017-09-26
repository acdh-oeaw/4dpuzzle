from django.http import HttpResponse
from django.core.serializers import serialize
from .models import Brick, Find, Stratunit


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
