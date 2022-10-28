from django.urls import path, include

from src.infrastructure.api.routes.user.routers import UserRouter
from src.infrastructure.api.views.user import UserViewSet

user_router = UserRouter()
user_router.register("", viewset=UserViewSet, basename="users")

urlpatterns = [path("", include(user_router.urls))]
