# Generated by Django 4.1 on 2022-09-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_category_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.CharField(default='DEV', max_length=3),
            preserve_default=False,
        ),
    ]