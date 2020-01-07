from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey

from archeutils.utils import get_category
from browsing.browsing_utils import model_to_dict
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
    )
    fc_arche_id = models.TextField(blank=True).set_extra(
        arche_prop="hasIdentifier",
    )
    fc_arche_description = models.TextField(blank=True).set_extra(
        arche_prop="hasDescription",
    )
    fc_arche_access = models.TextField(blank=True).set_extra(
        arche_prop="hasAccessRestriction",
    )
    fc_custom_rdf = models.TextField(blank=True)

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

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('filechecker:fccollection_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('filechecker:fccollection_create')

    def get_absolute_url(self):
        return reverse('filechecker:fccollection_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('filechecker:fccollection_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('filechecker:fccollection_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('filechecker:fccollection_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'filechecker:fccollection_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'filechecker:fccollection_detail',
                kwargs={'pk': prev.first().id}
            )
        return False


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
    fc_arche_access = models.TextField(
        blank=True,
        help_text="If set blank a given value from the parent directory\
        is taken for the rdf serialisation").set_extra(
        arche_prop="hasAccessRestriction",
    )
    fc_custom_rdf = models.TextField(blank=True)

    def __str__(self):
        return f"{self.fc_fullname}"

    def save(self, *args, **kwargs):
        self.fc_arche_id = filename_to_arche_id(self.fc_fullname)
        self.fc_arche_cat = get_category(self)
        super(FcResource, self).save(*args, **kwargs)
        return self

    def field_dict(self):
        return model_to_dict(self)

    @classmethod
    def get_listview_url(self):
        return reverse('filechecker:fcresource_browse')

    @classmethod
    def get_createview_url(self):
        return reverse('filechecker:fcresource_create')

    def get_absolute_url(self):
        return reverse('filechecker:fcresource_detail', kwargs={'pk': self.id})

    def get_absolute_url(self):
        return reverse('filechecker:fcresource_detail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('filechecker:fcresource_delete', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('filechecker:fcresource_edit', kwargs={'pk': self.id})

    def get_next(self):
        next = self.__class__.objects.filter(id__gt=self.id)
        if next:
            return reverse(
                'filechecker:fcresource_detail',
                kwargs={'pk': next.first().id}
            )
        return False

    def get_prev(self):
        prev = self.__class__.objects.filter(id__lt=self.id).order_by('-id')
        if prev:
            return reverse(
                'filechecker:fcresource_detail',
                kwargs={'pk': prev.first().id}
            )
        return False
