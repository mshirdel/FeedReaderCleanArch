from django.apps import AppConfig


class UserConfig(AppConfig):
    label = "user"
    name = "src.infrastructure.orm.db.user"
    verbose_name = "User"
