from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from . utils import as_arche_res


def as_arche_graph(request, app_name, model_name, pk):
    try:
        ct = ContentType.objects.get(app_label=app_name, model=model_name)
    except ObjectDoesNotExist:
        return JsonResponse({})
    try:
        int_pk = int(pk)
    except ValueError:
        return JsonResponse({})
    res = ct.model_class().objects.get(id=int_pk)
    g = as_arche_res(res)
    return HttpResponse(g.serialize(encoding='utf-8'), content_type='text/xml')
