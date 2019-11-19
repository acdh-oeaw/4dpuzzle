# generated by appcreator
import django_tables2 as tables
from django_tables2.utils import A
from . models import (
    Actor,
    ArchaeologicalObject4DPuzzleID,
    ArchaeologicalObjectID,
    ArchiveINF,
    AutoCAD,
    Convolutecards,
    Datenbase,
    Document4DPuzzleID,
    DocumentTypes,
    ExcavationObjectID,
    ExcavationSeasons,
    Fielddrawing,
    Film,
    Finddrawing,
    Findsheets,
    Fotoborndigital,
    Fotosgescannt,
    Fundinventar4DPuzzleID,
    FundinventarInventarnummern,
    FundinventarKonvolutnummern,
    FundinventarMaterialproben,
    FundinventarSteininventar,
    GIS,
    Geophysics,
    Inventorybooks,
    PhasenID,
    Protocols,
    StratenID,
    Tables,
    ThreeDimensionalModel,
    Videos,
    WallpaintingInventory
)


class ActorTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = Actor
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ArchaeologicalObject4DPuzzleIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = ArchaeologicalObject4DPuzzleID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ArchaeologicalObjectIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()
    corresponding_to_archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = ArchaeologicalObjectID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ArchiveINFTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = ArchiveINF
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class AutoCADTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = AutoCAD
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ConvolutecardsTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = Convolutecards
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class DatenbaseTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Datenbase
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class Document4DPuzzleIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = Document4DPuzzleID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class DocumentTypesTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = DocumentTypes
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ExcavationObjectIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    year = tables.columns.ManyToManyColumn()
    season = tables.columns.ManyToManyColumn()
    part_of_excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = ExcavationObjectID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ExcavationSeasonsTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = ExcavationSeasons
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FielddrawingTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    creator_metadata = tables.columns.ManyToManyColumn()
    creator_original = tables.columns.ManyToManyColumn()
    original_material = tables.columns.ManyToManyColumn()
    amendment_drawn_by = tables.columns.ManyToManyColumn()
    drawer_monogram = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Fielddrawing
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FilmTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = Film
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FinddrawingTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()

    class Meta:
        model = Finddrawing
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FindsheetsTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Findsheets
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FotoborndigitalTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Fotoborndigital
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FotosgescanntTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbreviation = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Fotosgescannt
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class Fundinventar4DPuzzleIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    relatedto = tables.columns.ManyToManyColumn()

    class Meta:
        model = Fundinventar4DPuzzleID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FundinventarInventarnummernTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()
    relatedto = tables.columns.ManyToManyColumn()

    class Meta:
        model = FundinventarInventarnummern
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FundinventarKonvolutnummernTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    find_material = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = FundinventarKonvolutnummern
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FundinventarMaterialprobenTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = FundinventarMaterialproben
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class FundinventarSteininventarTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    excavation_object_id = tables.columns.ManyToManyColumn()
    relatedto = tables.columns.ManyToManyColumn()

    class Meta:
        model = FundinventarSteininventar
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class GISTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()
    relatedto = tables.columns.ManyToManyColumn()

    class Meta:
        model = GIS
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class GeophysicsTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Geophysics
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class InventorybooksTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    find_inventory_number = tables.columns.ManyToManyColumn()

    class Meta:
        model = Inventorybooks
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class PhasenIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    area = tables.columns.ManyToManyColumn()
    containing_phase_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = PhasenID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ProtocolsTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Protocols
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class StratenIDTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    area = tables.columns.ManyToManyColumn()
    containing_stratum_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = StratenID
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class TablesTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()
    relatedto = tables.columns.ManyToManyColumn()

    class Meta:
        model = Tables
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class ThreeDimensionalModelTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = ThreeDimensionalModel
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class VideosTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')
    document_subtype = tables.columns.ManyToManyColumn()
    dst_abbr = tables.columns.ManyToManyColumn()
    excavation_object_id = tables.columns.ManyToManyColumn()
    archaeological_object_id = tables.columns.ManyToManyColumn()

    class Meta:
        model = Videos
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}


class WallpaintingInventoryTable(tables.Table):

    id = tables.LinkColumn(verbose_name='ID')

    class Meta:
        model = WallpaintingInventory
        sequence = ('id',)
        attrs = {"class": "table table-responsive table-hover"}
