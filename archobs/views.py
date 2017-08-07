from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Brick, Find, Stratunit


class BrickDetailView(DetailView):

    model = Brick
    template_name = 'archobs/brick_detail.html'


class FindDetailView(DetailView):

    model = Find
    template_name = 'archobs/brick_detail.html'


class StratunitDetailView(DetailView):

    model = Stratunit
    template_name = 'archobs/brick_detail.html'


class MainPageView(TemplateView):
    template_name = 'archobs/index.html'
