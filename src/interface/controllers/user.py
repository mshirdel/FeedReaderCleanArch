from typing import Tuple, Dict
from http import HTTPStatus

from marshmallow import ValidationError

from src.domain.user import UserEntity
from src.interface.repositories.exceptions import EntityDoesNotExist
from src.interface.serializers.user import UserSerializer
from src.usecases.user import UserInteractor


class UserController:
    def __init__(self, user_interactor: UserInteractor):
        self.user_interactor = user_interactor

    def create(self, params: Dict) -> Tuple[Dict, int]:
        try:
            user_data = UserSerializer().load(params)
        except ValidationError as err:
            return {"error": err.messages}, HTTPStatus.BAD_REQUEST.value
        user = self.user_interactor.save(UserEntity(user_data))
        return (
            UserSerializer.dump(user),
            HTTPStatus.CREATED.value,
        )  # todo check returned message

    def get(self, username: str) -> Tuple[Dict, int]:
        try:
            user = self.user_interactor.get(username)
        except EntityDoesNotExist as err:
            return {"error": err.message}, HTTPStatus.NOT_FOUND.value
        return UserSerializer().dump(user), HTTPStatus.OK.value
