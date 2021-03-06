from django.conf.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", include("projects.urls")),
    path("api/", include("api.urls")),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
]
