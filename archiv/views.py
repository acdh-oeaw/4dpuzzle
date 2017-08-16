from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Fielddrawing


class FielddrawingDetailView(DetailView):

    model = Fielddrawing
