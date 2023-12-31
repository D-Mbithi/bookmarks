from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("accounts/", include("accounts.urls")),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
