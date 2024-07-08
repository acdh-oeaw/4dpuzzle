from django.urls import path
from . import views

app_name = "webpage"

urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    path("", views.GenericWebpageView.as_view(), name="start"),
    path("accounts/login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("project-info/", views.project_info, name="project_info"),
    path("<slug:template>", views.GenericWebpageView.as_view(), name="staticpage"),
]
