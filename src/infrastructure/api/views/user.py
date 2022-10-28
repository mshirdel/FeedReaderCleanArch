from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from src.interface.controllers.user import UserController


class UserViewSet(ViewSet):
    viewset_factory = None

    @property
    def controller(self) -> UserController:
        return self.viewset_factory.create()

    def get(self, request: Request, username: str, *args, **kwargs) -> Response:
        payload, status = self.controller.get(username)
        return Response(data=payload, status=status)

    def create(self, request: Request, *args, **kwargs) -> Response:
        payload, status = self.controller.create(**kwargs)
        return Response(data=payload, status=status)
