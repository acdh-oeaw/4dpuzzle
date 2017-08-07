from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^brick/(?P<pk>[0-9]+)$', views.BrickDetailView.as_view(),  name='brick-detail'),
    url(r'^find/(?P<pk>[0-9]+)$', views.FindDetailView.as_view(),  name='find-detail'),
    url(
        r'^stratunit/(?P<pk>[0-9]+)$', views.StratunitDetailView.as_view(),  name='stratunit-detail'
    ),
]
