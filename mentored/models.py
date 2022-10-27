"""Models for mentores app."""

from django.db import models


class Profile(models.Model):
    """This model keep information about a mentored."""

    birthdate = models.DateField()

    def __str__(self):
        return self.statement
