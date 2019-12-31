from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from archeutils.utils import directory_to_col_id, get_category
from vocabs.models import SkosConcept

from . filechecker_utils import filename_to_arche_id


class FcCollection(MPTTModel):
    fc_fullname = models.TextField()
    fc_name = models.TextField()
    fc_ordername = models.CharField(blank=True, max_length=254)
    fc_lastmod = models.DateTimeField(null=True)
    fc_size = models.BigIntegerField(default=0)
    fc_items = models.BigIntegerField(default=0)
    parent = TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children'
    )
    fc_arche_id = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['fc_ordername']

    def __str__(self):
        return f"{self.fc_fullname}"

    def save(self, *args, **kwargs):

        self.fc_name = self.fc_fullname.split('/')[-2]
        self.fc_ordername = self.fc_name[:254]
        self.fc_arche_id = directory_to_col_id(self, path_prop="fc_fullname")
        super(FcCollection, self).save(*args, **kwargs)
        return self


class FcResource(models.Model):
    fc_fullname = models.TextField()
    fc_filename = models.TextField(blank=True, null=True)
    fc_lastmod = models.DateTimeField(null=True)
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
    fc_arche_cat = models.TextField(blank=True, null=True)
    fc_arche_id = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fc_fullname}"

    def save(self, *args, **kwargs):
        self.fc_arche_id = filename_to_arche_id(self.fc_fullname)
        self.fc_arche_cat = get_category(self)
        super(FcResource, self).save(*args, **kwargs)
        return self
