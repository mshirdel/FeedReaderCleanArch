import dataclasses
import json

from src.domain.user import UserEntity
from src.infrastructure.orm.db.user.models import User
from src.interface.repositories.exceptions import EntityDoesNotExist
from src.infrastructure.orm.db.user.tasks import save_user_task


class UserDatabaseRepository:
    def get(self, username: str) -> UserEntity:
        user = User.objects.filter(username=username).values().first()
        if not user:
            raise EntityDoesNotExist(f"username: ({username}) does not exist")
        return UserEntity(**user)

    def save(self, user: UserEntity):
        user_json = json.dumps(dataclasses.asdict(user))
        save_user_task.apply_async(kwargs={"user_json": user_json})
