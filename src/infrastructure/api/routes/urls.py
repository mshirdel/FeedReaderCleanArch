from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path("", include(f"src.infrastructure.api.routes.user.urls")),
    # path("", include(f"src.infrastructure.api.routes.feed.urls"))
]
