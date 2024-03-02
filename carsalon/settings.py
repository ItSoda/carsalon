import os
from datetime import timedelta
from pathlib import Path

from decouple import Config, RepositoryEnv
from django.utils import timezone

docker = os.environ.get("DOCKER_CONTAINER")
test = os.environ.get("REDIS_TEST")
env_file = ".env"

if docker:
    env_file = "docker-compose.env"

if test:
    env_file = "test.env"

config = Config(RepositoryEnv(env_file))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.get("DEBUG", default=True)

DOMAIN_NAME = config.get("DOMAIN_NAME")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "djoser",
    "channels",
    "rest_framework",
    "rest_framework_simplejwt.token_blacklist",
    "drf_yasg",
    "corsheaders",
    "cars",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "carsalon.urls"

# LOGGING
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "main_format": {
            "format": "{asctime} - {levelname} - {module} - {filename} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "main_format",
        },
    },
    "loggers": {
        "main": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "carsalon.wsgi.application"
ASGI_APPLICATION = "carsalon.asgi.application"

# PARAMETRS FOR DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config.get("MYSQL_DATABASE"),
        "USER": config.get("MYSQL_ROOT_USER"),
        "PASSWORD": config.get("MYSQL_ROOT_PASSWORD"),
        "HOST": config.get("MYSQL_HOST"),
        "PORT": config.get("MYSQL_PORT"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
if docker:
    STATIC_ROOT = "static"
else:
    STATICFILES_DIRS = [BASE_DIR / "static"]

# Base url to serve media files
MEDIA_URL = "/media/"
# Path where media is stored
MEDIA_ROOT = "media"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redis
REDIS_HOST = config.get("REDIS_HOST", "127.0.0.1")
REDIS_PORT = 6379
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# DRF
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}


# CSRF
CSRF_TRUSTED_ORIGINS = [
    "https://boar-still-alpaca.ngrok-free.app",
    "http://fohowomsk.ru",
    "https://fohowomsk.ru",
    "https://rest.nexmo.com",
]

# CORS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:50000",
    "http://localhost:3000",
    "http://fohowomsk.ru",
    "https://rest.nexmo.com",
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_URLS_REGEX = r"^/.*$"

# DEBUG TOOLBAR

INTERNAL_IPS = ["127.0.0.1", "localhost"]
