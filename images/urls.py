from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ScanListView.as_view(), name='scan_list'),
    url(r'^(?P<pk>[0-9]+)$', views.ScanDetailView.as_view(), name='scan_detail'),
    # url(r'^create/$', views.ScanCreate.as_view(), name='image_create'),
    # url(r'^update/(?P<pk>[0-9]+)$', views.ScanUpdate.as_view(), name='image_update'),
]
