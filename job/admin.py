from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Company
from .models import Job

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Job)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','main_stacks', 'main_skills', 'pay_range')
    search_fields = ['id','main_stacks', 'main_skills']

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'overview', 'website', 'industry', 'size', 'headquarters', 'founded', 'specialties')
    search_fields = ['id', 'name', 'industry', 'headquarters', 'founded', 'specialties']

class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_posted', 'type', 'location', 'requirements', 'link', 'category_id', 'company_id')
    search_fields = ['id', 'title', 'date_posted', 'type', 'locatiion', 'requirements', 'category_id', 'company_id']