from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Brick, Find, Stratunit, ExObject


class BrickDetailView(DetailView):

    model = Brick


class FindDetailView(DetailView):

    model = Find


class StratunitDetailView(DetailView):

    model = Stratunit


class ExObjectDetailView(DetailView):

    model = ExObject
