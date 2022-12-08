"""
Django settings for mentorship project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import io
import logging
import os
import secrets
from pathlib import Path
from types import MappingProxyType
from urllib.parse import urlparse

import environ
from django.core.exceptions import ImproperlyConfigured
from google import auth
from google.cloud import secretmanager

logger = logging.getLogger(__name__)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, '.env')

if os.path.isfile(env_file):
    environ.Env.read_env(env_file)
else:
    # Attempt to load the Project ID into the environment,
    # safely failing on error.
    try:  # noqa: WPS229
        credentials, project_id = auth.default()
        os.environ['GOOGLE_CLOUD_PROJECT'] = project_id
    except auth.exceptions.DefaultCredentialsError:
        logger.debug('Running without Gcloud')

    if os.environ.get('GOOGLE_CLOUD_PROJECT', None):
        # Pull secrets from Secret Manager
        project_id = os.environ.get('GOOGLE_CLOUD_PROJECT')

        client = secretmanager.SecretManagerServiceClient()
        settings_name = os.environ.get(
            'SETTINGS_NAME', 'mentorship-backend-django-settings',
        )
        name = 'projects/{0}/secrets/{1}/versions/latest'.format(
            project_id, settings_name,
        )
        response = client.access_secret_version(name=name)
        payload = response.payload.data.decode('UTF-8')

        env.read_env(io.StringIO(payload))
    else:
        raise ImproperlyConfigured(
            (
                'No local .env or GOOGLE_CLOUD_PROJECT detected.' +
                'No secrets found.'
            ),
        )

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default=secrets.token_urlsafe())
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

# [START cloudrun_django_csrf]
# SECURITY WARNING: It's recommended that you use this when
# running in production. The URL will be known once you first deploy
# to Cloud Run.
# This code takes the URL and converts it to both these settings formats.
CLOUDRUN_SERVICE_URL = env('CLOUDRUN_SERVICE_URL', default=None)
if CLOUDRUN_SERVICE_URL:
    ALLOWED_HOSTS = (urlparse(CLOUDRUN_SERVICE_URL).netloc,)
    CSRF_TRUSTED_ORIGINS = (CLOUDRUN_SERVICE_URL)
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
else:
    ALLOWED_HOSTS = ('*',)

# [END cloudrun_django_csrf]
# Application definition

INSTALLED_APPS = (
    'mentored.apps.MentoredConfig',
    'tech.apps.TechConfig',
    'job.apps.JobConfig',
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mentorship.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
)

WSGI_APPLICATION = 'mentorship.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = MappingProxyType({'default': env.db()})

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

VALIDATOR_NAME = 'NAME'

AUTH_PASSWORD_VALIDATORS = (
    {
        VALIDATOR_NAME: (
            (
                'django.contrib.auth.password_validation' +
                '.UserAttributeSimilarityValidator'
            )
        ),
    },
    {
        VALIDATOR_NAME: (
            'django.contrib.auth.password_validation.MinimumLengthValidator'
        ),
    },
    {
        VALIDATOR_NAME: (
            'django.contrib.auth.password_validation.CommonPasswordValidator'
        ),
    },
    {
        VALIDATOR_NAME: (
            'django.contrib.auth.password_validation.NumericPasswordValidator'
        ),
    },
)


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

GS_BUCKET_NAME = env('GS_BUCKET_NAME', default=None)

if GS_BUCKET_NAME:
    STATIC_URL = 'https://storage.googleapis.com/{0}/'.format(GS_BUCKET_NAME)
else:
    STATIC_URL = '/static/'

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'staticfiles'),
    )

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = MappingProxyType({
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination'
    ),
    'PAGE_SIZE': 10,
})
