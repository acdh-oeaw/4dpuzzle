from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bricks/$', views.BrickListView.as_view(), name='browse_bricks'),
]
