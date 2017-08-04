from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .models import Brick


class BrickDetailView(DetailView):

    model = Brick
    template_name = 'archobs/brick_detail.html'


class MainPageView(TemplateView):
    template_name = 'archobs/index.html'
