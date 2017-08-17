from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Fielddrawing, Foto


class FielddrawingDetailView(DetailView):

    model = Fielddrawing


class FotoDetailView(DetailView):

    model = Foto
