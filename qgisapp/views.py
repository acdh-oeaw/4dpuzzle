from django.views.generic import TemplateView


class QgisMapView(TemplateView):
    template_name = 'qgisapp/qgis_map.html'
