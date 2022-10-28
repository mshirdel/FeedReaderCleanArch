from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserEntity:
    username: str = None
    first_name: str = None
    last_name: str = None
    email: str = None
    is_staff: bool = False
    is_active: bool = True
    date_joined: datetime = None
    password: str = None
    last_login: datetime = None

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def to_string(user: "UserEntity") -> str:
        return user.fullname
