from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import *


class BrickDetailView(DetailView):

    model = Brick


class FindDetailView(DetailView):

    model = Find


class StratunitDetailView(DetailView):

    model = Stratunit


class ExcavationObjectDetailView(DetailView):

    model = ExcavationObject


class ExObjectDetailView(DetailView):

    model = ExObject
