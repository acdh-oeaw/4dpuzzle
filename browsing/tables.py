import django_tables2 as tables
from django_tables2.utils import A
from archobs.models import *
from archiv.models import Fielddrawing, Foto
from images.models import Scan


class ScanTable(tables.Table):
    id = tables.LinkColumn(
        'images:scan_detail', args=[A('pk')])

    class Meta:
        model = Scan
        fields = ['id', 'scan_type', 'creator_scan']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class BrickTable(tables.Table):
    id = tables.LinkColumn(
        'archobs:brick-detail', args=[A('pk')])

    class Meta:
        model = Brick
        fields = ['id', 'stratum_gi', 'brick_type']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class FindTable(tables.Table):
    id = tables.LinkColumn(
        'archobs:find-detail', args=[A('pk')])

    class Meta:
        model = Find
        fields = ['id', 'stratum_gi', 'find_type', 'find_mater']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class StratunitTable(tables.Table):
    id = tables.LinkColumn(
        'archobs:stratunit-detail', args=[A('pk')])

    class Meta:
        model = Stratunit
        fields = ['id', 'stratum_gi', 'resources_field']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class FielddrawingTable(tables.Table):
    id = tables.LinkColumn(
        'archiv:fielddrawing-detail', args=[A('pk')])

    class Meta:
        model = Stratunit
        fields = ['id', 'document_id', 'year']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class FotoTable(tables.Table):
    id = tables.LinkColumn(
        'archiv:foto-detail', args=[A('pk')])

    class Meta:
        model = Stratunit
        fields = ['id', 'document_id', 'year']
        attrs = {"class": "table table-hover table-striped table-condensed"}
