import json

from celery import shared_task

from src.infrastructure.orm.db.user.models import User


@shared_task
def save_user_task(user_json: str):
    user = json.loads(user_json)
    User.objects.create_user(
        username=user.username, email=user.email, password=user.password
    )
