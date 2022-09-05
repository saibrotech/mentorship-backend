# https://docs.djangoproject.com/en/4.0/topics/db/models/

from unicodedata import category
from django.db import models

# Create your models here.
class Language(models.Model):
    lang_name = models.CharField(max_length=20)
    lang_type = models.CharField(max_length=20)
    origin_country = models.CharField(max_length=20)
    origin_year = models.DateField()

