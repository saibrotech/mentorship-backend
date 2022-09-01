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


class Companies(models.Model):
    COMPANY_SIZES = (                   # Source: SEBRAE. Anuario do Trabalho na Micro e Pequena Empresa. Sebrae: Brasília. p.17. 2013.
        ('XS', 'Up to 10 employees'),   # https://www.sebrae.com.br/Sebrae/Portal%20Sebrae/Anexos/Anuario%20do%20Trabalho%20Na%20Micro%20e%20Pequena%20Empresa_2013.pdf
        ('S', '10 to 49 employees'),
        ('M', '50 to 99 employees'),
        ('L', 'Over 100 employees')
    )
    
    company_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    overview = models.TextField()
    website = models.CharField(max_length=200)
    industry = models.CharField(max_length=50)
    size = models.CharField(max_length=2, choices=COMPANY_SIZES)
    headquarters = models.CharField(max_length=50)
    founded = models.CharField(max_length=4)
    specialties = models.TextField()