import os

from django.core.wsgi import get_wsgi_application

env = os.environ.get("DJANGO_ENV")
settings_module = f"src.infrastructure.settings.{env}"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()
