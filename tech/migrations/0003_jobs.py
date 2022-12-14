# Generated by Django 4.1 on 2022-08-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech', '0002_language_origin_country_language_origin_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('listing_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('experience_level', models.CharField(choices=[('INTERN', 'Internship'), ('ENTRY', 'Entry Level'), ('ASSOC', 'Associate')], max_length=6)),
                ('type', models.CharField(choices=[('FULL', 'Full-time'), ('PART', 'Part-time'), ('CONTR', 'Contract'), ('INTERN', 'Internship'), ('OTHER', 'Other')], max_length=6)),
                ('location', models.CharField(max_length=50)),
                ('requirements', models.TextField()),
                ('link', models.CharField(max_length=200)),
            ],
        ),
    ]
