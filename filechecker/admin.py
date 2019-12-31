from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . models import FcCollection, FcResource


admin.site.register(FcCollection, MPTTModelAdmin)
admin.site.register(FcResource)
