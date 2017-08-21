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
    objectid = models.FloatField(blank=True)
    gisfind_id = models.CharField(blank=True, max_length=250)
    excavation = models.CharField(blank=True, max_length=250)
    stratum_id = models.CharField(blank=True, max_length=250)
    stratum_gi = models.CharField(blank=True, max_length=250)
    phase_id = models.CharField(blank=True, max_length=250)
    phase_gis_field = models.CharField(blank=True, max_length=250)
    archaeolog = models.CharField(blank=True, max_length=250)
    gis_locus_field = models.CharField(blank=True, max_length=250)
    gis_su_id = models.CharField(blank=True, max_length=250)
    gis_commen = models.CharField(blank=True, max_length=250)
    find_mater = models.CharField(blank=True, max_length=250)
    find_type = models.CharField(blank=True, max_length=250)
    height = models.FloatField(blank=True)
    find_inven = models.CharField(blank=True, max_length=250)
    find_local = models.CharField(blank=True, max_length=250)
    eigner_map = models.CharField(blank=True, max_length=250)
    resource_i = models.CharField(blank=True, max_length=250)
    geom = models.MultiPointField(srid=4326)

    def iiifjson(self):
        return "https://iiif.acdh.oeaw.ac.at/p4d/TD_F-I_j21/{}__{}/info.json".format(
            self.resource_i, self.excavation
        ).replace(' ', '').replace('lanum_', 'lanum')

    def __str__(self):
        return "{}".format(self.gisfind_id)

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
    objectid = models.FloatField(blank=True, null=True)
    gisbrick_i = models.CharField(blank=True, max_length=250)
    excavation = models.CharField(blank=True, max_length=250)
    stratum_id = models.CharField(blank=True, max_length=250)
    stratum_gi = models.CharField(blank=True, max_length=250)
    phase_id = models.CharField(blank=True, max_length=250)
    phase_gis_field = models.CharField(blank=True, max_length=250)
    archaeolog = models.CharField(blank=True, max_length=250)
    archaeol_1 = models.CharField(blank=True, max_length=250)
    archaeol_2 = models.CharField(blank=True, max_length=250)
    gis_su_id = models.CharField(blank=True, max_length=250)
    gis_locus_field = models.CharField(blank=True, max_length=250)
    brick_type = models.CharField(blank=True, max_length=250)
    brick_mate = models.CharField(blank=True, max_length=250)
    height_max = models.FloatField(blank=True, null=True)
    extrusion = models.FloatField(blank=True, null=True)
    orientatio = models.CharField(blank=True, max_length=250)
    resource_i = models.CharField(blank=True, max_length=250)
    base_heigh = models.FloatField(blank=True, null=True)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def iiifjson(self):
        return "https://iiif.acdh.oeaw.ac.at/p4d/TD_F-I_j21/{}__{}/info.json".format(
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
        return "{}".format(self.gisbrick_i)


class Stratunit(models.Model):
    objectid = models.FloatField(blank=True, null=True)
    type = models.CharField(blank=True, max_length=250)
    gis_su_id = models.CharField(blank=True, max_length=250)
    excavation = models.CharField(blank=True, max_length=250)
    stratum_id = models.CharField(blank=True, max_length=250)
    stratum_gi = models.CharField(blank=True, max_length=250)
    phase_id = models.CharField(blank=True, max_length=250)
    phase_gis_field = models.CharField(blank=True, max_length=250)
    locus_id = models.CharField(blank=True, max_length=250)
    archaeolog = models.CharField(blank=True, max_length=250)
    archaeol_1 = models.CharField(blank=True, max_length=250)
    archaeol_2 = models.CharField(blank=True, max_length=250)
    height_top = models.FloatField(blank=True, null=True)
    height_t_1 = models.FloatField(blank=True, null=True)
    height_bot = models.FloatField(blank=True, null=True)
    height_b_1 = models.FloatField(blank=True, null=True)
    extrusion = models.FloatField(blank=True, null=True)
    base_heigh = models.FloatField(blank=True, null=True)
    eigner_map = models.CharField(blank=True, max_length=250)
    resources_field = models.CharField(blank=True, max_length=250)
    pit_fill = models.CharField(blank=True, max_length=250)
    pit_find_g = models.CharField(blank=True, max_length=250)
    bp_materia = models.CharField(blank=True, max_length=250)
    bp_door_st = models.CharField(blank=True, max_length=250)
    bp_door_1 = models.CharField(blank=True, max_length=250)
    wall_type = models.CharField(blank=True, max_length=250)
    wall_brick = models.CharField(blank=True, max_length=250)
    wall_inter = models.CharField(blank=True, max_length=250)
    wall_bri_1 = models.CharField(blank=True, max_length=250)
    locus_laye = models.CharField(blank=True, max_length=250)
    shape_clas = models.CharField(blank=True, max_length=250)
    orientatio = models.CharField(blank=True, max_length=250)
    stratum = models.CharField(blank=True, max_length=250)
    phase = models.CharField(blank=True, max_length=250)
    wall_funct = models.CharField(blank=True, max_length=250)
    su_nummer = models.CharField(blank=True, max_length=250)
    wall_conne = models.CharField(blank=True, max_length=250)
    old_object = models.CharField(blank=True, max_length=250)
    shape_leng = models.FloatField(blank=True, null=True)
    shape_area = models.FloatField(blank=True, null=True)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return "{}".format(self.gis_su_id)

    def iiifjson(self):
        return "https://iiif.acdh.oeaw.ac.at/p4d/TD_F-I_j21/{}__{}/info.json".format(
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
