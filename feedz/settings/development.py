from feedz.settings.base import *  # noqa

SECRET_KEY = "django-insecure-omd9rdz$vea#!d_!54rhq0w=g9==)xhk8b#goq0innp9)+mmb#"

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "feedz",
        "USER": "meysam",
        "PASSWORD": "pg123",
        "HOST": "localhost",
        "PORT": "5432",
    },
}

INSTALLED_APPS += ["debug_toolbar"]  # noqa
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa
