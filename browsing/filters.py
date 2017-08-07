import django_filters
from . import forms
from browsing.forms import *
from archobs.models import *
from vocabs.models import *
from places.models import *

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


class BrickListFilter(django_filters.FilterSet):
    class Meta:
        model = Brick
        fields = ['stratum_id', 'phase_id', 'brick_type']


class FindListFilter(django_filters.FilterSet):
    class Meta:
        model = Find
        fields = ['stratum_id', 'phase_id', 'find_type']


class StratunitListFilter(django_filters.FilterSet):
    class Meta:
        model = Stratunit
        fields = ['stratum_id', 'phase_id', 'resources_field']
