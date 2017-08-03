from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ImageListView.as_view(), name='image_list'),
    url(r'^(?P<pk>[0-9]+)$', views.ImageDetailView.as_view(), name='image_detail'),
    # url(r'^create/$', views.ImageCreate.as_view(), name='image_create'),
    # url(r'^update/(?P<pk>[0-9]+)$', views.ImageUpdate.as_view(), name='image_update'),
]
