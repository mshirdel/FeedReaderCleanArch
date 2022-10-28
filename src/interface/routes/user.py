from src.domain.core.constants import HTTP_VERB_GET, HTTP_VERB_POST
from src.domain.core.routing import Router, Route
from src.interface.controllers.user import UserController
from src.interface.routes.constants import USERS_PREFIX

user_router = Router()
user_router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=rf"^{USERS_PREFIX}/(?P<username>[a-zA-Z]+)/$",
            controller=UserController,
            method="get",
            name="users_get",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=rf"^{USERS_PREFIX}/$",
            controller=UserController,
            method="create",
            name="users_create",
        ),
    ]
)
