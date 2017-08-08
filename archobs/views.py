from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Brick, Find, Stratunit


class BrickDetailView(DetailView):

    model = Brick


class FindDetailView(DetailView):

    model = Find


class StratunitDetailView(DetailView):

    model = Stratunit


class MainPageView(TemplateView):
    template_name = 'archobs/index.html'
