from django.db import models
from vocabs.models import SkosConcept
from images.models import Image


class Person(models.Model):
    fullname = models.CharField(max_length=300, blank=True)
    name = models.CharField(max_length=300, blank=True)
    surname = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.fullname)


class ArchObject(models.Model):
    name = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.object_type)


class ExObject(models.Model):
    name = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.object_type)


class Site(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Area(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class SquareTrench(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Planum(models.Model):
    name = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return "{}".format(self.name)


class Scan(Image):
    creator_scan = models.ManyToManyField(Person, blank=True, related_name='creator_scan')
    scan_date = models.DateField(blank=True, null=True)
    equipment = models.ForeignKey(SkosConcept, blank=True, null=True)
    resolution = models.CharField(max_length=300, blank=True, null=True)


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
    exobject = models.ManyToManyField(ExObject, blank=True)
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
    document_id = models.CharField(max_length=500, blank=True)
    document_type = models.ManyToManyField(SkosConcept, blank=True, related_name="document_type")
    document_subtype = models.ManyToManyField(
        SkosConcept, blank=True, related_name="document_subtype"
    )
    scan = models.ManyToManyField(Scan, blank=True)
    site = models.ForeignKey(Site, blank=True, null=True)
    area = models.ForeignKey(Area, blank=True, null=True)
    square_trence = models.ManyToManyField(SquareTrench, blank=True)
    planum = models.ManyToManyField(Planum, blank=True)
    perspective_of_drawing = models.ManyToManyField(SkosConcept, blank=True)
    stratum_commentary = models.CharField(max_length=300, blank=True)
    drawn_by = models.ManyToManyField(Person, blank=True)
    year = models.CharField(max_length=300, blank=True)
    season = models.ManyToManyField(SkosConcept, blank=True, related_name="season")
    month = models.ManyToManyField(SkosConcept, blank=True, related_name="month")
    scale = models.ManyToManyField(SkosConcept, blank=True, related_name="scale")
    paper_type = models.ManyToManyField(SkosConcept, blank=True, related_name="paper_type")
    archobject = models.ManyToManyField(ArchObject, blank=True)
    exobject = models.ManyToManyField(ExObject, blank=True)

    def __str__(self):
        return "{}".format(self.document_id)

    def iiifjson(self):
        try:
            scan = self.scan.all()[0]
        except:
            scan = None

        return "{}".format(scan)

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
