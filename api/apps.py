"""App confoguration for API layer."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Api configuration App."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
