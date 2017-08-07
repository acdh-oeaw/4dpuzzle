import django_tables2 as tables
from django_tables2.utils import A
from archobs.models import *


class BrickTable(tables.Table):
    id = tables.LinkColumn(
        'archobs:brick-detail', args=[A('pk')], verbose_name='cbab-id')

    class Meta:
        model = Brick
        fields = ['id', 'stratum_gi', 'brick_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}
