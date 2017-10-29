import django_filters
from dal import autocomplete
from . import forms
from browsing.forms import *
from archobs.models import *
from vocabs.models import *
from places.models import *
from archiv.models import Fielddrawing, Foto
from images.models import Scan
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


class ExcavationObjectListFilter(django_filters.FilterSet):

    class Meta:
        model = ExcavationObject
        exclude = ['geom']


class ScanListFilter(django_filters.FilterSet):

    class Meta:
        model = Scan
        fields = ['creator_scan', 'equipment', 'resolution', 'scan_type']


class ExObjectListFilter(django_filters.FilterSet):

    class Meta:
        model = ExObject
        fields = ['name']


class ArchivBaseFilter(django_filters.FilterSet):
    area = django_filters.ModelChoiceFilter(queryset=Area.objects.all())
    square_trence = django_filters.ModelMultipleChoiceFilter(
        queryset=SquareTrench.objects
    )
    planum = django_filters.ModelMultipleChoiceFilter(
        queryset=Planum.objects
    )


class FielddrawingListFilter(django_filters.FilterSet):
    #archobject = django_filters.ModelMultipleChoiceFilter(queryset=ArchObject.objects)
    class Meta:
        model = Fielddrawing
        #exclude = ['scan']
        fields = ['area', 'square_trence', 'planum','year', 'document_id']


class FotoListFilter(django_filters.FilterSet):
    #foto_type = django_filters.ModelMultipleChoiceFilter(queryset=FotoType.objects)
    class Meta:
        model = Foto
        fields = [ 'film_number','photo_number','foto_type','year', 'document_id']


class BrickListFilter(django_filters.FilterSet):

    class Meta:
        model = Brick
        exclude = ['geom']


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
        exclude = ['geom']


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
        exclude = ['geom']
