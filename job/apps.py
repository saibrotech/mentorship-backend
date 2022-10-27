"""App configuration for Job App."""

from django.apps import AppConfig


class JobConfig(AppConfig):
    """Configuration for job App."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'job'
