from django.urls import path
from . import views

app_name = "browsing"

urlpatterns = [
    path("merge-objects/", views.merge_objects, name="merge_objects"),
]
