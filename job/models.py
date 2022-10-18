from tabnanny import verbose
from django.db import models
from unicodedata import category

# https://docs.djangoproject.com/en/4.0/topics/db/models/


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)
    main_stacks = models.CharField(max_length=200)
    main_skills = models.CharField(max_length=200)
    pay_range = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        verbose_name_plural = 'Categories'


class Company(models.Model):
    COMPANY_SIZES = [                   # Source: SEBRAE. Anuario do Trabalho na Micro e Pequena Empresa. Sebrae: Brasília. p.17. 2013.
        # https://www.sebrae.com.br/Sebrae/Portal%20Sebrae/Anexos/Anuario%20do%20Trabalho%20Na%20Micro%20e%20Pequena%20Empresa_2013.pdf
        ('XS', 'Up to 10 employees'),
        ('S', '10 to 49 employees'),
        ('M', '50 to 99 employees'),
        ('L', 'Over 100 employees')
    ]

    name = models.CharField(max_length=50)
    overview = models.TextField()
    website = models.CharField(max_length=200)
    industry = models.CharField(max_length=50)
    size = models.CharField(max_length=2, choices=COMPANY_SIZES)
    headquarters = models.CharField(max_length=50)
    founded = models.CharField(max_length=4)
    specialties = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.id})'

    class Meta:
        verbose_name_plural = 'Companies'


class Job(models.Model):
    XP_LEVELS = [
        ('INTERN', 'Internship'),
        ('ENTRY', 'Entry Level'),
        ('ASSOC', 'Associate')
    ]

    JOB_TYPES = [
        ('FULL', 'Full-time'),
        ('PART', 'Part-time'),
        ('CONTR', 'Contract'),
        ('INTERN', 'Internship'),
        ('OTHER', 'Other')
    ]

    title = models.CharField(max_length=50)
    date_posted = models.DateField()
    experience_level = models.CharField(max_length=6, choices=XP_LEVELS)
    type = models.CharField(max_length=6, choices=JOB_TYPES)
    location = models.CharField(max_length=50)
    requirements = models.TextField()
    link = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
