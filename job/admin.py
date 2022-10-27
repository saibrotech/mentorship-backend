"""Admin configuration for job App."""

from django.contrib import admin

# Register your models here.
from job.models import Category, Company, Job

FIELD_ID = 'id'
FIELD_NAME = 'name'


class CategoryAdmin(admin.ModelAdmin):
    """Category admin configuration."""

    list_display = (
        FIELD_ID,
        FIELD_NAME,
        'main_stacks',
        'main_skills',
        'pay_range',
    )
    search_fields = (FIELD_ID, FIELD_NAME, 'main_stacks', 'main_skills')


class CompanyAdmin(admin.ModelAdmin):
    """Company admin configuration."""

    list_display = (
        FIELD_ID,
        FIELD_NAME,
        'overview',
        'website',
        'industry',
        'size',
        'headquarters',
        'founded',
        'specialties',
    )
    search_fields = [
        FIELD_ID,
        FIELD_NAME,
        'industry',
        'headquarters',
        'founded',
        'specialties',
    ]


class JobAdmin(admin.ModelAdmin):
    """Job admin configuration ."""

    list_display = (
        FIELD_ID,
        'title',
        'type',
        'location',
        'requirements',
        'link',
        'category_id',
        'company_id',
        'date_posted',
    )
    search_fields = [FIELD_ID, 'title', 'type', 'location', 'requirements']
    list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
