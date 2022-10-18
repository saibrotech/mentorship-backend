# https://docs.djangoproject.com/en/4.0/topics/db/models/

from django.db import models


class Profile(models.Model):
    birthdate = models.DateField()
