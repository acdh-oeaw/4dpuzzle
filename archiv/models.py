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
    resolution = models.IntegerField(blank=True, null=True)


class Fielddrawing(models.Model):
    document_id = models.URLField(blank=True)
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
        return "https://iiif.acdh.oeaw.ac.at/p4d/TD_F-I_j21/{}/info.json".format(
            self.document_id
        ).replace(' ', '')

    def __str__(self):
        return "{}".format(self.document_id)

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
