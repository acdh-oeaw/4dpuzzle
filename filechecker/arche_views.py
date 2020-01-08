from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from . models import FcCollection, FcResource

from . arche_serializer import as_arche_graph, qs_as_arche_res, get_root_col


def res_as_arche_graph(request, model_name, pk):
    format = request.GET.get('format', 'xml')
    try:
        ct = ContentType.objects.get(app_label='filechecker', model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: filechecker defined")
    try:
        int_pk = int(pk)
    except ValueError:
        raise Http404(f"No model: {model_name} with id: {pk} found")
    try:
        res = ct.model_class().objects.get(id=int_pk)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} with id: {pk} found")
    g = as_arche_graph(res)
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )


def qs_as_arche_graph(request, model_name):
    format = request.GET.get('format', 'xml')
    try:
        start = int(request.GET.get('start', 0))
    except ValueError:
        start = 0
    try:
        end = int(request.GET.get('end', 10))
    except ValueError:
        end = 10
    try:
        ct = ContentType.objects.get(app_label='filechecker', model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: filechecker defined")
    qs = ct.model_class().objects.all()[start:end]
    g = qs_as_arche_res(qs)
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )


def children_as_arche_graph(request, pk):
    format = request.GET.get('format', 'xml')
    try:
        int_pk = int(pk)
    except ValueError:
        raise Http404(f"No FcCollection with id: {pk} found")
    try:
        res = FcCollection.objects.get(id=int_pk)
    except ObjectDoesNotExist:
        raise Http404(f"No FcCollection with id: {pk} found")
    g = as_arche_graph(res)
    qs = FcResource.objects.filter(fc_directory=res)
    if len(qs) > 0:
        children_graph = qs_as_arche_res(qs)
        g = g + children_graph
    ancestors = res.get_ancestors()
    print(ancestors)
    if len(ancestors) > 0:
        g = g + qs_as_arche_res(ancestors)
    g = g + get_root_col()
    if format == 'turtle':
        return HttpResponse(
            g.serialize(encoding='utf-8', format='turtle'), content_type='text/turtle'
        )
    else:
        return HttpResponse(
            g.serialize(encoding='utf-8'), content_type='application/xml'
        )
