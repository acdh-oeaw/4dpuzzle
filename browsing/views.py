from django.shortcuts import render
from django_tables2 import SingleTableView, RequestConfig
from archobs.models import *
from .filters import *
from .forms import GenericFilterFormHelper
from .tables import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class GenericListView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'
    paginate_by = 25

    def get_queryset(self, **kwargs):
        qs = super(GenericListView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super(GenericListView, self).get_table()
        RequestConfig(self.request, paginate={
            'page': 1, 'per_page': self.paginate_by}).configure(table)
        return table

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context


class ScanListView(GenericListView):
    model = Scan
    table_class = ScanTable
    template_name = 'browsing/scan_list_generic.html'
    filter_class = ScanListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ScanListView, self).dispatch(*args, **kwargs)


class FotoListView(GenericListView):
    model = Foto
    table_class = FotoTable
    template_name = 'browsing/foto_list_generic.html'
    filter_class = FotoListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FotoListView, self).dispatch(*args, **kwargs)


class FielddrawingListView(GenericListView):
    model = Fielddrawing
    table_class = FielddrawingTable
    template_name = 'browsing/fielddrawing_list_generic.html'
    filter_class = FielddrawingListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(FielddrawingListView, self).dispatch(*args, **kwargs)


class BrickListView(GenericListView):
    model = Brick
    table_class = BrickTable
    template_name = 'browsing/brick_list_generic.html'
    filter_class = BrickListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class FindListView(GenericListView):
    model = Find
    table_class = FindTable
    template_name = 'browsing/find_list_generic.html'
    filter_class = FindListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context


class StratunitListView(GenericListView):
    model = Stratunit
    table_class = StratunitTable
    template_name = 'browsing/stratunit_list_generic.html'
    filter_class = StratunitListFilter
    formhelper_class = GenericFilterFormHelper

    def get_context_data(self, **kwargs):
        context = super(GenericListView, self).get_context_data()
        context[self.context_filter_name] = self.filter

        return context