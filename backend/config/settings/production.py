from .base import *

DEBUG = False
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "school_db",
        "USER": "DB_USER",
        "PASSWORD": "DB_PSWD",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
