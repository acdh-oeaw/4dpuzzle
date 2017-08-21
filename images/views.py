from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Image, Scan


class ScanDetailView(DetailView):
    model = Scan
    template_name = 'images/scan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ScanDetailView, self).get_context_data(**kwargs)
        # try:
        #     context["next_entry"] = Scan.objects.filter(id__gt=int(self.kwargs['pk']))[0].pk
        # except:
        #     context["next_entry"] = None
        # try:
        #     prev = [x.id for x in Scan.objects.filter(id__lt=int(self.kwargs['pk']))][-1]
        # except:
        #     prev = Scan.objects.get(id=self.kwargs['pk'])
        # try:
        #     Scan.objects.get(id=int(prev)-1)
        #     context["previous_entry"] = prev
        # except:
        #     context["previous_entry"] = None

        return context

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ScanDetailView, self).dispatch(*args, **kwargs)


class ScanListView(ListView):
    model = Scan
    template_name = 'images/image_list.html'

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ScanListView, self).dispatch(*args, **kwargs)
