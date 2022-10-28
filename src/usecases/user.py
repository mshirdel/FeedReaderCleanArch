from src.domain.user import UserEntity


class UserInteractor:
    def __init__(self, user_repo: object):
        self._user_repo = user_repo

    def get(self, username: str) -> UserEntity:
        return self._user_repo.get(username)

    def save(self, user: UserEntity):
        self._user_repo.save(user)
