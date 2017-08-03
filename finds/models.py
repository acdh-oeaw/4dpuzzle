from django.contrib.gis.db import models
from stratunits.models import Stratunit


# This is derived from an auto-generated Django model module created by ogrinspect.
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
    stratunit = models.ForeignKey(Stratunit, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.gisfind_id)
