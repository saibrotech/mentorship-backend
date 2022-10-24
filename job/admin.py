from django.contrib import admin

# Register your models here.
from .models import Category, Company, Job


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_stacks', 'main_skills', 'pay_range')
    search_fields = ['id', 'name', 'main_stacks', 'main_skills']


class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'overview',
        'website',
        'industry',
        'size',
        'headquarters',
        'founded',
        'specialties')
    search_fields = [
        'id',
        'name',
        'industry',
        'headquarters',
        'founded',
        'specialties']


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'type',
        'location',
        'requirements',
        'link',
        'category_id',
        'company_id',
        'date_posted')
    search_fields = ['id', 'title', 'type', 'location', 'requirements']
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
