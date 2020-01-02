from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from . utils import as_arche_res, qs_as_arche_res


def res_as_arche_graph(request, app_name, model_name, pk):
    try:
        ct = ContentType.objects.get(app_label=app_name, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_name} defined")
    try:
        int_pk = int(pk)
    except ValueError:
        raise Http404(f"No model: {model_name} with id: {pk} found")
    res = ct.model_class().objects.get(id=int_pk)
    g = as_arche_res(res)
    return HttpResponse(g.serialize(encoding='utf-8'), content_type='application/xml')


def qs_as_arche_graph(request, app_name, model_name):
    start = 0
    page_size = 100
    try:
        ct = ContentType.objects.get(app_label=app_name, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_name} defined")
    qs = ct.model_class().objects.all()
    maingraph = qs_as_arche_res(qs[start:page_size])
    return HttpResponse(maingraph.serialize(encoding='utf-8'), content_type='application/xml')
