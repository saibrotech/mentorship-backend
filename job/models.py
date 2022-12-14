"""Model classes for job App."""

from django.db import models


class Category(models.Model):
    """Job Category."""

    name_length = 50
    code_lenght = 3
    main_length = 200
    pay_range_length = 10

    name = models.CharField(max_length=name_length)
    code = models.CharField(max_length=code_lenght)
    main_stacks = models.CharField(max_length=main_length)
    main_skills = models.CharField(max_length=main_length)
    pay_range = models.CharField(max_length=pay_range_length)

    class Meta(object):
        verbose_name_plural = 'Categories'

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.id)


class Company(models.Model):
    """Company with jobs."""

    name_length = 50
    industry_length = 50
    headquarters_length = 50
    code_lenght = 3
    website_length = 200
    pay_range_length = 10
    founded_length = 4
    size_length = 2

    # Source: SEBRAE. Anuario do Trabalho na Micro e Pequena Empresa.
    # Sebrae: Brasília. p.17. 2013.
    # https://www.sebrae.com.br/Sebrae/Portal%20Sebrae/Anexos/Anuario
    # %20do%20Trabalho%20Na%20Micro%20e%20Pequena%20Empresa_2013.pdf
    company_sizes = [
        ('XS', 'Up to 10 employees'),
        ('S', '10 to 49 employees'),
        ('M', '50 to 99 employees'),
        ('L', 'Over 100 employees'),
    ]

    name = models.CharField(max_length=name_length)
    overview = models.TextField()
    website = models.CharField(max_length=website_length)
    industry = models.CharField(max_length=industry_length)
    size = models.CharField(max_length=size_length, choices=company_sizes)
    headquarters = models.CharField(max_length=headquarters_length)
    founded = models.CharField(max_length=founded_length)
    specialties = models.TextField()

    class Meta(object):
        verbose_name_plural = 'Companies'

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.id)


class Job(models.Model):
    """Job in IT."""

    title_length = 50
    experience_level_length = 6
    type_length = 6
    location_length = 50
    link_length = 200

    xp_levels = [
        ('INTERN', 'Internship'),
        ('ENTRY', 'Entry Level'),
        ('ASSOC', 'Associate'),
    ]

    job_types = [
        ('FULL', 'Full-time'),
        ('PART', 'Part-time'),
        ('CONTR', 'Contract'),
        ('INTERN', 'Internship'),
        ('OTHER', 'Other'),
    ]

    title = models.CharField(max_length=title_length)
    date_posted = models.DateField()
    experience_level = models.CharField(
        max_length=experience_level_length,
        choices=xp_levels,
    )
    type = models.CharField(max_length=type_length, choices=job_types)
    location = models.CharField(max_length=location_length)
    requirements = models.TextField()
    link = models.CharField(max_length=link_length)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta(object):
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return '{0} ({1})'.format(self.title, self.id)
