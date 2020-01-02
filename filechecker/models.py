from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from archeutils.utils import get_category
from vocabs.models import SkosConcept

from . filechecker_utils import filename_to_arche_id, remove_trailing_slash


def set_extra(self, **kwargs):
    self.extra = kwargs
    return self


models.Field.set_extra = set_extra


class FcCollection(MPTTModel):
    fc_fullname = models.TextField()
    fc_name = models.TextField().set_extra(
        arche_prop="hasTitle",
    )
    fc_ordername = models.CharField(blank=True, max_length=254)
    fc_firstmod = models.DateTimeField(null=True).set_extra(
        arche_prop="hasCollectedStartDate",
    )
    fc_lastmod = models.DateTimeField(null=True).set_extra(
        arche_prop="hasCollectedEndDate",
    )
    fc_size = models.BigIntegerField(default=0)
    fc_items = models.BigIntegerField(default=0)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    ).set_extra(
        arche_prop="isPartOf",
    )
    fc_arche_id = models.TextField(blank=True).set_extra(
        arche_prop="hasIdentifier",
    )
    fc_arche_description = models.TextField(blank=True).set_extra(
        arche_prop="hasDescription",
    )

    class MPTTMeta:
        order_insertion_by = ['fc_ordername']

    def __str__(self):
        return f"{self.fc_fullname}"

    def save(self, *args, **kwargs):
        self.fc_fullname = remove_trailing_slash(self.fc_fullname)
        try:
            self.fc_name = self.fc_fullname.split('/')[-1]
        except IndexError:
            self.fc_name = self.fc_fullname
        self.fc_ordername = self.fc_name
        self.fc_arche_id = filename_to_arche_id(self.fc_fullname)
        super(FcCollection, self).save(*args, **kwargs)
        return self


class FcResource(models.Model):
    fc_fullname = models.TextField()
    fc_filename = models.TextField(blank=True, null=True).set_extra(
        arche_prop="hasTitle",
    )
    fc_lastmod = models.DateTimeField(null=True).set_extra(
        arche_prop="hasDate",
    )
    fc_size = models.BigIntegerField(blank=True, null=True)
    fc_directory = models.ForeignKey(
        FcCollection,
        on_delete=models.CASCADE, null=True, blank=True,
        related_name='has_fc_resource'
    )
    fc_type = models.CharField(
        blank=True, null=True, max_length=254
    )
    fc_extension = models.CharField(
        blank=True, null=True, max_length=254
    )
    fc_arche_cat = models.TextField(blank=True, null=True).set_extra(
        arche_prop="hasCategory",
    )
    fc_arche_id = models.TextField(blank=True).set_extra(
        arche_prop="hasIdentifier",
    )
    fc_arche_description = models.TextField(blank=True).set_extra(
        arche_prop="hasDescription",
    )

    def __str__(self):
        return f"{self.fc_fullname}"

    def save(self, *args, **kwargs):
        self.fc_arche_id = filename_to_arche_id(self.fc_fullname)
        self.fc_arche_cat = get_category(self)
        super(FcResource, self).save(*args, **kwargs)
        return self
