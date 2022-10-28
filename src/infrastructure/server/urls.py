from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/", include((f"src.infrastructure.api.routes.urls", "api"), namespace="api")
    ),
]
