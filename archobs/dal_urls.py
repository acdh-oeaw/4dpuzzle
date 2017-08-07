from django.conf.urls import url
from . import views
from . import dal_views
from .models import *


urlpatterns = [
    url(
        r'^strat-dal/$',
        dal_views.StratAC.as_view(),
        name='strat-dal',
    ),
]
