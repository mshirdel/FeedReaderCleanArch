from rest_framework.routers import SimpleRouter, Route

from src.infrastructure.factories.user import UserViewSetFactory
from src.interface.routes.user import user_router


class UserRouter(SimpleRouter):
    routes = [
        Route(
            url=user_router.get_url("users_get"),
            mapping=user_router.map("users_get"),
            initkwargs={"viewset_factory": UserViewSetFactory},
            name="{basename}-get",
            detail=False,
        ),
        # Route(
        #     url=user_router.get_url("users_create"),
        #     mapping=user_router.map("users_create"),
        #     initkwargs={"viewset_factory": UserViewSetFactory},
        #     name='{base_name}-create',
        #     detail=False,
        # )
    ]
