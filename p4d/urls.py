from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from vocabs import api_views

router = routers.DefaultRouter()
router.register(r"metadata", api_views.MetadataViewSet)
router.register(r"skoslabels", api_views.SkosLabelViewSet)
router.register(r"skosnamespaces", api_views.SkosNamespaceViewSet)
router.register(r"skosconceptschemes", api_views.SkosConceptSchemeViewSet)
router.register(r"skoscollections", api_views.SkosCollectionViewSet)
router.register(r"skosconcepts", api_views.SkosConceptViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("admin/", admin.site.urls),
    path("archeutils/", include("archeutils.urls", namespace="archeutils")),
    path(
        "filechecker-rdf/",
        include("filechecker.fc_arche_urls", namespace="filechecker-rdf"),
    ),
    path("filechecker/", include("filechecker.urls", namespace="filechecker")),
    path("browsing/", include("browsing.urls", namespace="browsing")),
    path("netvis/", include("netvis.urls", namespace="netvis")),
    path("info/", include("infos.urls", namespace="info")),
    path("archiv/", include("archiv.urls", namespace="archiv")),
    path("qgisapp/", include("qgisapp.urls", namespace="qgisapp")),
    path("vocabs/", include("vocabs.urls", namespace="vocabs")),
    path("vocabs-ac/", include("vocabs.dal_urls", namespace="vocabs-ac")),
    path("", include("webpage.urls", namespace="webpage")),
]
