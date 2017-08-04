from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^brick/(?P<pk>[0-9]+)$', views.BrickDetailView.as_view(),  name='brick-detail'),
]
