from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'bricks/$', views.BrickListView.as_view(), name='browse_bricks'),
    url(r'finds/$', views.FindListView.as_view(), name='browse_finds'),
    url(r'stratunits/$', views.StratunitListView.as_view(), name='browse_stratunits'),
    url(r'fielddrawings/$', views.FielddrawingListView.as_view(), name='browse_fielddrawings'),
    url(r'fotos/$', views.FotoListView.as_view(), name='browse_fotos'),
    url(r'scans/$', views.ScanListView.as_view(), name='browse_scans'),
]
