# Generated by Django 4.1 on 2022-09-05 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0005_category_company_job_delete_companies_delete_jobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='category_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='company_id',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]