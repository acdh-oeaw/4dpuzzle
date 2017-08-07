from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bricks/$', views.BrickListView.as_view(), name='browse_bricks'),
    url(r'finds/$', views.FindListView.as_view(), name='browse_finds'),
    url(r'stratunits/$', views.StratunitListView.as_view(), name='browse_stratunits'),
]
