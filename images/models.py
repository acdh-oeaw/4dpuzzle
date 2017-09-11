import os
from django.db import models
from django.conf import settings
from places.models import Person
from vocabs.models import SkosConcept

try:
    base_url = settings.IIIF_BASE
except:
    base_url = "https://iiif.acdh.oeaw.ac.at/"

IIIF_PATH = "{}{}".format(base_url, os.path.basename(settings.BASE_DIR))
FILE_EXTENSION_CHOICES = (
    ('.tif', 'tif'),
    ('.jpg', '.jpg'),
)


class ServerPath(models.Model):
    name = models.CharField(default=IIIF_PATH, blank=True, max_length=250)

    def __str__(self):
        return "{}".format(self.name)


class Image(models.Model):
    path = models.ForeignKey(ServerPath, blank=True, null=True)
    directory = models.CharField(blank=True, max_length=250)
    filename = models.CharField(blank=True, max_length=250)
    file_extension = models.CharField(
        blank=True, max_length=20, choices=FILE_EXTENSION_CHOICES, default='.jpg')

    class Meta:
        abstract = True

    def get_next(self):
        next = Image.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Image.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def save(self, *args, **kwargs):
        if self.path is None:
            temp_path, _ = ServerPath.objects.get_or_create(name=IIIF_PATH)
            self.path = temp_path
        else:
            pass
        super(Image, self).save(*args, **kwargs)

    @property
    def full_path(self):
        if self.directory == "":
            return "{}/{}/info.json".format(self.path, self.filename)
        else:
            return "{}{}/{}/info.json".format(self.path, self.directory, self.filename)

    def __str__(self):
        return self.full_path

    @property
    def iiif_endpoint(self):
        if self.directory == "":
            return "{}/{}".format(self.path, self.filename)
        else:
            return "{}{}/{}".format(self.path, self.directory, self.filename)

    def __str__(self):
        return self.full_path


class Scan(Image):
    creator_scan = models.ManyToManyField(Person, blank=True, related_name='creator_scan')
    scan_date = models.DateField(blank=True, null=True)
    equipment = models.ForeignKey(SkosConcept, blank=True, null=True)
    resolution = models.CharField(max_length=300, blank=True, null=True)
    scan_type = models.ForeignKey(SkosConcept, blank=True, null=True, related_name="scan_type")

    def get_next(self):
        next = Scan.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Scan.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def save(self, *args, **kwargs):
        if self.path is None:
            temp_path, _ = ServerPath.objects.get_or_create(name=IIIF_PATH)
            self.path = temp_path
        else:
            pass
        super(Scan, self).save(*args, **kwargs)

    @property
    def full_path(self):
        if self.directory == "":
            return "{}/{}/info.json".format(self.path, self.filename)
        else:
            return "{}{}/{}/info.json".format(self.path, self.directory, self.filename)

    def __str__(self):
        return self.full_path

    @property
    def iiif_endpoint(self):
        if self.directory == "":
            return "{}/{}".format(self.path, self.filename)
        else:
            return "{}{}/{}".format(self.path, self.directory, self.filename)

    def __str__(self):
        return self.full_path
