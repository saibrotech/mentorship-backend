# https://docs.djangoproject.com/en/4.0/topics/db/models/

from django.db import models

# Create your models here.
class Language(models.Model):
    lang_name = models.CharField(max_length=20)
    lang_type = models.CharField(max_length=20)
    origin_country = models.CharField(max_length=20)
    origin_year = models.DateField()

class Jobs(models.Model):
    XP_LEVELS = (
        ('INTERN', 'Internship'),
        ('ENTRY', 'Entry Level'),
        ('ASSOC', 'Associate')
    )

    JOB_TYPES = (
        ('FULL', 'Full-time'),
        ('PART', 'Part-time'),
        ('CONTR', 'Contract'),
        ('INTERN', 'Internship'),
        ('OTHER', 'Other')
    )

    listing_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    date_posted = models.DateField
    experience_level = models.CharField(max_length=6, choices=XP_LEVELS)
    type = models.CharField(max_length=6, choices=JOB_TYPES)
    location = models.CharField(max_length=50)
    requirements = models.TextField()
    link = models.CharField(max_length=200)    