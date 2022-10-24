""" ."""

# https://docs.djangoproject.com/en/4.0/topics/db/models/

from django.db import models

# Create your models here.


class Language(models.Model):
    """ ."""

    size = 20
    lang_name = models.CharField(max_length=size)
    lang_type = models.CharField(max_length=size)
    origin_country = models.CharField(max_length=size)
    origin_year = models.DateField()

    def __str__(self):
        """ ."""
        return self.statement
