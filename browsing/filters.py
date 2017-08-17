import django_filters
from dal import autocomplete
from . import forms
from browsing.forms import *
from archobs.models import *
from vocabs.models import *
from places.models import *
from archiv.models import Fielddrawing, Foto

# To do: django_filters.MethodFilter are commented because raising errors after version upgrade
# test and remove if not needed anymore

django_filters.filters.LOOKUP_TYPES = [
    ('', '---------'),
    ('exact', 'Is equal to'),
    ('iexact', 'Is equal to (case insensitive)'),
    ('not_exact', 'Is not equal to'),
    ('lt', 'Lesser than/before'),
    ('gt', 'Greater than/after'),
    ('gte', 'Greater than or equal to'),
    ('lte', 'Lesser than or equal to'),
    ('startswith', 'Starts with'),
    ('endswith', 'Ends with'),
    ('contains', 'Contains'),
    ('icontains', 'Contains (case insensitive)'),
    ('not_contains', 'Does not contain'),
]


class FielddrawingListFilter(django_filters.FilterSet):

    class Meta:
        model = Fielddrawing
        fields = '__all__'


class FotoListFilter(django_filters.FilterSet):

    class Meta:
        model = Foto
        fields = ['document_id', 'archobject']


class BrickListFilter(django_filters.FilterSet):

    stratum_id = django_filters.CharFilter(
        widget=autocomplete.Select2(
            url='archobs-dal:strat-dal',
            # attrs={'data-minimum-input-length': 1}
        ),
        lookup_expr='icontains',
        label='Name',
        help_text=False,
    )

    class Meta:
        model = Brick
        fields = ['phase_id', 'brick_type']


class FindListFilter(django_filters.FilterSet):

    stratum_id = django_filters.CharFilter(
        widget=autocomplete.Select2(
            url='archobs-dal:strat-dal',
            # attrs={'data-minimum-input-length': 1}
        ),
        lookup_expr='icontains',
        label='Name',
        help_text=False,
    )

    class Meta:
        model = Find
        fields = ['phase_id', 'find_type']


class StratunitListFilter(django_filters.FilterSet):

    stratum_id = django_filters.CharFilter(
        widget=autocomplete.Select2(
            url='archobs-dal:strat-dal',
            # attrs={'data-minimum-input-length': 1}
        ),
        lookup_expr='icontains',
        label='Name',
        help_text=False,
    )

    class Meta:
        model = Stratunit
        fields = ['phase_id', 'resources_field']
