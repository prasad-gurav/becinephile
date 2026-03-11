"""
Django base settings for becinephile.

Use: DJANGO_SETTINGS_MODULE=becinephile.config.settings
(or config.settings when run from becinephile/ as cwd)
"""
import os
from pathlib import Path

import environ

# Build paths: repository root = parent of becinephile/
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# Project root (becinephile/)
PROJECT_DIR = Path(__file__).resolve().parent.parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
    SECRET_KEY=(str, ""),
)

# Read .env from repository root (optional)
env_file = BASE_DIR / ".env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

# ----- Security -----
SECRET_KEY = env("SECRET_KEY")
if not SECRET_KEY and env.bool("DEBUG", False):
    SECRET_KEY ="django-insecure-secret-key"

DEBUG = env("DEBUG")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third-party
    "rest_framework",
    "rest_framework_simplejwt",
    "corsheaders",
    "dj_rest_auth",
    "django_extensions",
    "rest_framework.authtoken",
    # Local
    "core",
    "bookings",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"

# ----- Templates -----
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
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

# ----- Database -----
DATABASES = {
    "default": env.db(
        "DATABASE_URL",
        default="sqlite:///" + str(PROJECT_DIR / "db.sqlite3").replace("\\", "/"),
    ),
}

# ----- Auth -----
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----- Internationalization -----
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----- Static & Media -----
STATIC_URL = "static/"
STATIC_ROOT = env("STATIC_ROOT", default=str(PROJECT_DIR / "staticfiles"))

MEDIA_URL = "media/"
MEDIA_ROOT = env("MEDIA_ROOT", default=str(PROJECT_DIR / "media"))

# ----- Default primary key -----
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ----- REST Framework -----
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}

# ----- CORS (tune in env-specific settings) -----
CORS_ALLOW_ALL_ORIGINS = env.bool("CORS_ALLOW_ALL_ORIGINS", default=DEBUG)
