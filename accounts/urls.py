from django.urls import path, include
from django.views.generic import TemplateView

from . import views

# app_name = "accounts"

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path(
        "profile/",
        TemplateView.as_view(template_name="account/profile.html"),
        name="profile",
    ),
]
