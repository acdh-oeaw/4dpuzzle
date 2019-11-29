import django_tables2 as tables
from django_tables2.utils import A

from browsing.browsing_utils import MergeColumn
from vocabs.models import *


class SkosLabelTable(tables.Table):
    name = tables.LinkColumn('vocabs:skoslabel_detail', args=[A('pk')])
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = SkosLabel
        sequence = ['id', 'name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SkosConceptSchemeTable(tables.Table):
    dc_title = tables.LinkColumn('vocabs:skosconceptscheme_detail', args=[A('pk')])
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = SkosConceptScheme
        sequence = ['id', 'dc_title']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SkosCollectionTable(tables.Table):
    name = tables.LinkColumn('vocabs:skoscollection_detail', args=[A('pk')])
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = SkosCollection
        sequence = ['id', 'name']
        attrs = {"class": "table table-hover table-striped table-condensed"}


class SkosConceptTable(tables.Table):
    broader_concept = tables.Column(verbose_name='Broader Term')
    pref_label = tables.LinkColumn('vocabs:skosconcept_detail', args=[A('pk')])
    all_schemes = tables.Column(verbose_name='in SkosScheme', orderable=False)
    merge = MergeColumn(verbose_name='keep | remove', accessor='pk')

    class Meta:
        model = SkosConcept
        sequence = ['broader_concept', 'pref_label', 'all_schemes', 'namespace']
        attrs = {"class": "table table-hover table-striped table-condensed"}
