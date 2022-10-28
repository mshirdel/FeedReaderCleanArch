from src.infrastructure.orm.db.user.repositories import UserDatabaseRepository
from src.interface.controllers.user import UserController
from src.interface.repositories.user import UserRepository
from src.usecases.user import UserInteractor


class UserViewSetFactory:
    @staticmethod
    def create() -> UserController:
        user_interactor = UserInteractorFactory.get()
        return UserController(user_interactor)


class UserDatabaseRepositoryFactory:
    @staticmethod
    def get() -> UserDatabaseRepository:
        return UserDatabaseRepository()


class UserRepositoryFactory:
    @staticmethod
    def get() -> UserRepository:
        db_repo = UserDatabaseRepositoryFactory.get()
        cache_repo = None
        return UserRepository(db_repo=db_repo, cache_repo=cache_repo)


class UserInteractorFactory:
    @staticmethod
    def get() -> UserInteractor:
        user_repo = UserRepositoryFactory.get()
        return UserInteractor(user_repo)
