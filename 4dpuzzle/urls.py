from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from places.apis_views import PlaceViewSet
from bib.api_views import BookViewSet

from vocabs import api_views

router = routers.DefaultRouter()
router.register(r'skoslabels', api_views.SkosLabelViewSet)
router.register(r'skosnamespaces', api_views.SkosNamespaceViewSet)
router.register(r'skosconceptschemes', api_views.SkosConceptSchemeViewSet)
router.register(r'skosconcepts', api_views.SkosConceptViewSet)
router.register(r'places', PlaceViewSet)
router.register(r'Book', BookViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^sparql/', include('sparql.urls', namespace='sparql')),
    url(r'^browsing/', include('browsing.urls', namespace='browsing')),
    url(r'^vocabs/', include('vocabs.urls', namespace='vocabs')),
    url(r'^vocabs-ac/', include('vocabs.dal_urls', namespace='vocabs-ac')),
    url(r'^datamodel/', include('django_spaghetti.urls', namespace='datamodel')),
    url(r'places/', include('places.urls', namespace='places')),
    url(r'^bib/', include('bib.urls', namespace='bib')),
    url(r'^images/', include('images.urls', namespace='images')),
    url(r'^archobs-json/', include('archobs.api_urls', namespace='archobs-json')),
    url(r'^archobs-dal/', include('archobs.dal_urls', namespace='archobs-dal')),
    url(r'^archobs/', include('archobs.urls', namespace='archobs')),
    url(r'^archiv/', include('archiv.urls', namespace='archiv')),
    url(r'^', include('webpage.urls', namespace='webpage')),
]
