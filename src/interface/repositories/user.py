from typing import List

from src.domain.user import UserEntity


class UserRepository:
    def __init__(self, db_repo: object, cache_repo: object):
        self.db_repo = db_repo
        self.cache_repo = cache_repo

    def get(self, username: str) -> UserEntity:
        user = self.cache_repo.get(username) if self.cache_repo else None
        if not user:
            user = self.db_repo.get(username)
            if self.cache_repo:
                self.cache_repo.save(user)
        return user

    def list(self) -> List[UserEntity]:
        return self.db_repo.list()

    def save(self, user: UserEntity):
        self.db_repo.save(user)
