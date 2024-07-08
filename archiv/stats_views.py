from django.views.generic import TemplateView

from archeutils.utils import fetch_models

from .models import *


class MatchBinaryView(TemplateView):
    template_name = "archiv/match_stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        summary = []
        for x in fetch_models("archiv"):
            class_name = x.__name__
            items = x.objects.all()
            all_objects = items.count()
            match = items.exclude(fc_match=False).count()
            no_match = items.exclude(fc_match=True).count()
            try:
                percentage = (match / all_objects) * 100
            except:  # noqa:
                percentage = 0
            summary.append([class_name, all_objects, match, no_match, percentage])
            context["table_head"] = [
                "class_name",
                "all_objects",
                "match",
                "no_match",
                "percentage",
            ]
            context["table_body"] = summary
        return context
