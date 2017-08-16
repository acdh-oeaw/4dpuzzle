from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(
        r'^fielddrawing/(?P<pk>[0-9]+)$', views.FielddrawingDetailView.as_view(),
        name='fielddrawing-detail'
    ),
]
