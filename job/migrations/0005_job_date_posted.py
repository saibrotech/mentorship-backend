# Generated by Django 4.1 on 2022-10-18 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_rename_category_id_job_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_posted',
            field=models.DateField(default='2022-10-18'),
            preserve_default=False,
        ),
    ]
