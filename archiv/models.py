from django.db import models
from archobs.models import ArchObject, ExObject, Site, Area, SquareTrench, Planum, Find
from images.models import Scan
from places.models import Person
from vocabs.models import SkosConcept


class Foto(models.Model):
    composed_id = models.CharField(max_length=500, blank=True)
    document_id = models.CharField(max_length=300, blank=True)
    photo_title = models.CharField(max_length=300, blank=True)
    film_number = models.CharField(max_length=300, blank=True)
    film_id = models.CharField(max_length=300, blank=True)
    photo_number = models.CharField(max_length=300, blank=True)
    digital_photo_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='digital_photo_type'
    )
    foto_format = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name="foto_format"
    )
    photographer = models.ForeignKey(Person, blank=True, null=True)
    original_film_folder = models.CharField(max_length=20, blank=True)
    foto_type = models.ForeignKey(
        SkosConcept, blank=True, null=True, related_name='foto_type'
    )
    content_type = models.ManyToManyField(
        SkosConcept, blank=True, related_name="content_type"
    )
    site = models.ForeignKey(Site, blank=True, null=True)
    year = models.CharField(max_length=300, blank=True)
    archobject = models.ManyToManyField(ArchObject, blank=True)
    exobject = models.ManyToManyField(ExObject, blank=True, related_name="exobject_foto")
    scale = models.ForeignKey(SkosConcept, blank=True, null=True, related_name="foto_scale")
    metadata_creation_date = models.DateField(blank=True, null=True)
    metadata_creator = models.ManyToManyField(Person, blank=True, related_name="metadata_creator")
    metadata_comment = models.TextField(blank=True)
    scan = models.ManyToManyField(Scan, blank=True)

    def __str__(self):
        return "{}".format(self.composed_id)

    def iiifjson(self):
        try:
            scan = self.scan.all()[0]
        except:
            scan = None

        return "{}".format(scan)

    def get_next(self):
        next = Foto.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Foto.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class Fielddrawing(models.Model):
    document_id = models.CharField(
        max_length=500, blank=True,
        help_text="This is the unique identifier of the document. It consists of abbreviations for site_document type_inventory number (e.g.: ‘TD_FZ_1234’ means ‘Tell el-Daba_field drawing _1234’)."
    )
    document_type = models.ManyToManyField(
        SkosConcept, blank=True, related_name="document_type",
        help_text="Definition of resource type (in this case field drawing)"
    )
    document_subtype = models.ManyToManyField(
        SkosConcept, blank=True, related_name="document_subtype",
        help_text="Definition of the contains of the resource (e.g.: Planum, Profil, Detail, Sondage)"
    )
    scan = models.ManyToManyField(Scan, blank=True)
    perspective_of_drawing = models.ManyToManyField(
        SkosConcept, blank=True,
        help_text="Compass direction of drawer"
    )
    stratum_commentary = models.CharField(
        max_length=300, blank=True,
        help_text="Exact copy of the stratum commentary on the field drawing"
    )
    drawn_by = models.ManyToManyField(
        Person, blank=True,
        help_text="Autor/drawer"
    )
    year = models.CharField(
        max_length=300, blank=True, help_text="Year of the production of the field drawing"
    )
    season = models.ManyToManyField(
        SkosConcept, blank=True, related_name="season",
        help_text="Season of the production of the field drawing"
    )
    month = models.ManyToManyField(
        SkosConcept, blank=True, related_name="month",
        help_text="Month of the production of the field drawing"
    )
    scale = models.ManyToManyField(
        SkosConcept, blank=True, related_name="scale", help_text="Drawing scale"
    )
    paper_type = models.ManyToManyField(
        SkosConcept, blank=True, related_name="paper_type",
        help_text="Paper type e.g. graph paper, transparent paper, copy paper"
    )
    archobject = models.ManyToManyField(
        ArchObject, blank=True,
        help_text="Archaeological object ID contains: Abbreviation of site_area_square trench_description of archaeological object (e.g.: TD_F-I_o19_Grab1, TD_F-I_o19_Opfergrube4)",
        related_name="archobject_fielddrawing"
    )
    exobject = models.ManyToManyField(
        ExObject, blank=True, related_name="exobject_fielddrawing",
        help_text="Excavation object ID contains: Abbreviation of site_area_square trench_description of excavation object (e.g.: TD_F-I_o19_Planum1, TD_F-I_o19_Westprofil)"
    )
    site = models.ForeignKey(
        Site, blank=True, null=True,
        help_text="Archaeological site (here: Tell el Daba – TD)"
    )
    area = models.ForeignKey(
        Area, blank=True, null=True,
        help_text="Excavation area e.g.: F-I, A-II, H-III"
    )
    square_trence = models.ManyToManyField(
        SquareTrench, blank=True,
        help_text="Name of the square trench of the excavation area, taken from grid system e.g.: o21, k19"
    )
    planum = models.ManyToManyField(
        Planum, blank=True, help_text="Number of the planum (e.g.: Planum1, Planum2)"
    )

    def __str__(self):
        return "{}".format(self.document_id)

    def rel_archob_finds(self):
        libfinds = Find.objects.filter(orea_gis_i=self.document_id)
        if len(libfinds) > 0:
            return list(libfinds)
        else:
            return None

    def iiifjson(self):
        try:
            scan = self.scan.all()[0]
        except:
            scan = None

        return "{}".format(scan)

    def iiif_endpoint(self):
        try:
            scan = self.scan.all()[0]
        except:
            scan = None

        return "{}".format(scan.iiif_endpoint)

    def get_next(self):
        next = Fielddrawing.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Fielddrawing.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
