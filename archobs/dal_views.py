from dal import autocomplete
from .models import *
from django.db.models import Q


class StratAC(autocomplete.Select2ListView):
    def get_list(self):
        values = list(Brick.objects.all().values("stratum_id").distinct())
        values += list(Stratunit.objects.all().values("stratum_id").distinct())
        values += list(Find.objects.all().values("stratum_id").distinct())
        values = [x['stratum_id'] for x in values]
        return set(values)
