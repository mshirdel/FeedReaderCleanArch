from django.contrib.auth.models import AbstractUser

from src.domain.user import UserEntity


class User(AbstractUser):
    def __str__(self) -> str:
        return UserEntity.to_string(self)
