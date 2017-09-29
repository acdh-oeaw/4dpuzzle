from django.contrib.gis.db import models
from vocabs.models import SkosConcept


class ArchObject(models.Model):
    name = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True, null=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.object_type)


class ExObject(models.Model):
    name = models.CharField(max_length=300, blank=True)
    object_type = models.ForeignKey(SkosConcept, blank=True, null=True)

    def fetch_location(self):
        location_parts = self.name.split('_')
        if len(location_parts) != 4:
            parsed_location = {
                'Site': None,
                'Area': None,
                'SquareTrench': None,
                'Planum': None
            }
        else:
            parsed_location = {
                'Site': location_parts[0],
                'Area': location_parts[1],
                'SquareTrench': location_parts[2],
                'Planum': location_parts[3]
            }
        return parsed_location

    def get_next(self):
        next = ExObject.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = ExObject.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

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


class Find(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    orea_gis_i = models.CharField(blank=True, null=True, max_length=254)
    find_mater = models.CharField(blank=True, null=True, max_length=254)
    find_type = models.CharField(blank=True, null=True, max_length=254)
    excavation = models.CharField(blank=True, null=True, max_length=254)
    height = models.FloatField(blank=True, null=True)
    function = models.CharField(blank=True, null=True, max_length=254)
    archaeolog = models.CharField(blank=True, null=True, max_length=254)
    extrusion = models.FloatField(blank=True, null=True)
    base_heigh = models.FloatField(blank=True, null=True)
    find_local = models.CharField(blank=True, null=True, max_length=254)
    find_inven = models.CharField(blank=True, null=True, max_length=254)
    stratum_id = models.CharField(blank=True, null=True, max_length=254)
    stratum_gi = models.CharField(blank=True, null=True, max_length=254)
    phase_id = models.CharField(blank=True, null=True, max_length=254)
    phase_gis_field = models.CharField(blank=True, null=True, max_length=254)
    gis_commen = models.CharField(blank=True, null=True, max_length=254)
    eigner_map = models.CharField(blank=True, null=True, max_length=254)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    resources_field = models.CharField(max_length=254, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def iiifjson(self):
        return "https://4dpuzzle-iiif.acdh.oeaw.ac.at/{}__{}/info.json".format(
            self.resource_i, self.excavation
        ).replace(' ', '').replace('lanum_', 'lanum')

    def __str__(self):
        return "{}".format(self.orea_gis_i)

    def get_next(self):
        next = Find.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Find.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class FindSpot(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    orea_gis_i = models.CharField(blank=True, null=True, max_length=254)
    excavation = models.CharField(blank=True, null=True, max_length=254)
    stratum_id = models.CharField(blank=True, null=True, max_length=254)
    stratum_gi = models.CharField(blank=True, null=True, max_length=254)
    phase_id = models.CharField(blank=True, null=True, max_length=254)
    phase_gis_field = models.CharField(blank=True, null=True, max_length=254)
    archaeolog = models.CharField(blank=True, null=True, max_length=254)
    gis_commen = models.CharField(blank=True, null=True, max_length=254)
    find_mater = models.CharField(blank=True, null=True, max_length=254)
    find_type = models.CharField(blank=True, null=True, max_length=254)
    height = models.FloatField(blank=True, null=True)
    find_inven = models.CharField(blank=True, null=True, max_length=254)
    find_local = models.CharField(blank=True, null=True, max_length=254)
    eigner_map = models.CharField(blank=True, null=True, max_length=254)
    comments = models.CharField(blank=True, null=True, max_length=254)
    resources_field = models.CharField(blank=True, null=True, max_length=254)
    geom = models.MultiPointField(srid=4326)

    def iiifjson(self):
        return "https://4dpuzzle-iiif.acdh.oeaw.ac.at/{}__{}/info.json".format(
            self.resource_i, self.excavation
        ).replace(' ', '').replace('lanum_', 'lanum')

    def __str__(self):
        return "{}".format(self.orea_gis_i)

    def get_next(self):
        next = Find.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Find.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False


class Brick(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    orea_gis_i = models.CharField(blank=True, null=True, max_length=254)
    excavation = models.CharField(blank=True, null=True, max_length=254)
    stratum_id = models.CharField(blank=True, null=True, max_length=254)
    phase_id = models.CharField(blank=True, null=True, max_length=254)
    archaeolog = models.CharField(blank=True, null=True, max_length=254)
    archaeol_1 = models.CharField(blank=True, null=True, max_length=254)
    archaeol_2 = models.CharField(blank=True, null=True, max_length=254)
    brick_type = models.CharField(blank=True, null=True, max_length=254)
    brick_mate = models.CharField(blank=True, null=True, max_length=254)
    height_max = models.FloatField(blank=True, null=True)
    extrusion = models.FloatField(blank=True, null=True)
    base_heigh = models.FloatField(blank=True, null=True)
    orientatio = models.CharField(blank=True, null=True, max_length=254)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    resources_field = models.CharField(blank=True, null=True, max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def iiifjson(self):
        return "https://4dpuzzle-iiif.acdh.oeaw.ac.at/{}__{}/info.json".format(
            self.resource_i, self.excavation
        ).replace(' ', '').replace('lanum_', 'lanum')

    def get_next(self):
        next = Brick.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Brick.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False

    def __str__(self):
        return "{}".format(self.orea_gis_i)


class Stratunit(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    orea_gis_i = models.CharField(blank=True, null=True, max_length=254)
    excavation = models.CharField(blank=True, null=True, max_length=254)
    stratum_id = models.CharField(blank=True, null=True, max_length=254)
    phase_id = models.CharField(blank=True, null=True, max_length=254)
    locus_id = models.CharField(blank=True, null=True, max_length=254)
    locus_wall = models.CharField(blank=True, null=True, max_length=254)
    archaeolog = models.CharField(blank=True, null=True, max_length=254)
    archaeol_1 = models.CharField(blank=True, null=True, max_length=254)
    archaeol_2 = models.CharField(blank=True, null=True, max_length=254)
    height_top = models.FloatField(blank=True, null=True)
    height_t_1 = models.CharField(blank=True, null=True, max_length=254)
    height_bot = models.CharField(blank=True, null=True, max_length=254)
    height_b_1 = models.CharField(blank=True, null=True, max_length=254)
    extrusion = models.FloatField(blank=True, null=True)
    base_heigh = models.FloatField(blank=True, null=True)
    eigner_map = models.CharField(blank=True, null=True, max_length=254)
    pit_fill = models.CharField(blank=True, null=True, max_length=254)
    pit_find_g = models.CharField(blank=True, null=True, max_length=254)
    bp_materia = models.CharField(blank=True, null=True, max_length=254)
    bp_door_st = models.CharField(blank=True, null=True, max_length=254)
    bp_door_1 = models.CharField(blank=True, null=True, max_length=254)
    wall_type = models.CharField(blank=True, null=True, max_length=254)
    wall_cours = models.CharField(blank=True, null=True, max_length=254)
    wall_inter = models.CharField(blank=True, null=True, max_length=254)
    wall_brick = models.CharField(blank=True, null=True, max_length=254)
    locus_laye = models.CharField(blank=True, null=True, max_length=254)
    shape_clas = models.CharField(blank=True, null=True, max_length=254)
    orientatio = models.CharField(blank=True, null=True, max_length=254)
    wall_funct = models.CharField(blank=True, null=True, max_length=254)
    wall_conne = models.CharField(blank=True, null=True, max_length=254)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    resources_field = models.CharField(blank=True, null=True, max_length=254)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return "{}".format(self.orea_gis_i)

    def iiifjson(self):
        return "https://4dpuzzle-iiif.acdh.oeaw.ac.at/{}__{}/info.json".format(
            self.resources_field, (self.excavation)
        ).replace(' ', '').replace('lanum_', 'lanum')

    def get_next(self):
        next = Stratunit.objects.filter(id__gt=self.id)
        if next:
            return next.first().id
        return False

    def get_prev(self):
        prev = Stratunit.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return prev.first().id
        return False
