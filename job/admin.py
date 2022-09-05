from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Company
from .models import Job

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Job)
