import django_tables2 as tables
from django_tables2.utils import A
from archobs.models import *
from archiv.models import Fielddrawing, Foto
from images.models import Scan


class ExcavationObjectTable(tables.Table):
    id = tables.LinkColumn(
        'archobs:excavationobject-detail', args=[A('pk')])

    class Meta:
        model = ExcavationObject
        fields = ['id', 'orea_gis_i', 'excavation']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class ExObjectTable(tables.Table):
    id = tables.LinkColumn('archobs:exobject-detail', args=[A('pk')])

    class Meta:
        model = ExObject
        fields = ['id', 'name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


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
        fields = ['id', 'archaeolog', 'brick_type', 'brick_mate']
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
        fields = ['id', 'excavation', 'resources_field', 'archaeol_2']
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
