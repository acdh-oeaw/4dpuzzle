from django.apps import apps

from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType

from .utils import as_arche_res, qs_as_arche_res, resolve_p4d_id, fbd_as_arche


def fbd_arche_rdf(request, app_name, model_name):
    try:
        ct = ContentType.objects.get(app_label=app_name, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_name} defined")
    qs = ct.model_class().objects.all()
    g = fbd_as_arche(qs)
    return HttpResponse(
        g.serialize(encoding="utf-8", format="turtle"), content_type="text/turtle"
    )


def resolve_id_to_graph(request):
    p4d_id = request.GET["id"]
    res = resolve_p4d_id(p4d_id)
    try:
        res.id
    except AttributeError:
        raise Http404(f"No object with arche-id: {p4d_id} was found")
    g = as_arche_res(res)
    return HttpResponse(
        g.serialize(encoding="utf-8", format="turtle"), content_type="text/turtle"
    )


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
    return HttpResponse(
        g.serialize(encoding="utf-8", format="turtle"), content_type="text/turtle"
    )


def qs_as_arche_graph(request, app_name, model_name):
    try:
        start = int(request.GET.get("start", 0))
    except ValueError:
        start = 0
    try:
        page_size = int(request.GET.get("page_size", 100))
    except ValueError:
        page_size = 100

    if page_size > 100:
        page_size = 100

    page_size = start + page_size
    try:
        ct = ContentType.objects.get(app_label=app_name, model=model_name)
    except ObjectDoesNotExist:
        raise Http404(f"No model: {model_name} in app: {app_name} defined")
    qs = ct.model_class().objects.all()[start:page_size]
    maingraph = qs_as_arche_res(qs)
    return HttpResponse(
        maingraph.serialize(encoding="utf-8", format="turtle"),
        content_type="text/turtle",
    )


def relevante_classes(request, app_name):
    models = apps.get_app_config(app_name).get_models()
    base_uri = request.build_absolute_uri().split("/archeutils")[0]
    good_models = []
    for x in models:
        try:
            x.import_in_arche()
            item = {
                "class_name": f"{x.__name__.lower()}",
                "object_count": x.objects.all().count(),
                "endpoint": f"{base_uri}/archeutils/{app_name}/{x.__name__.lower()}?start=0&page_size=100",
            }
            good_models.append(item)
        except AttributeError:
            continue
    data = {"app_name": app_name, "models": good_models}
    return JsonResponse(data)
