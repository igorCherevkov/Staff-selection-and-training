# Generated by Django 4.2.4 on 2023-11-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0017_alter_companyvacancy_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='companyvacancy',
            name='info',
            field=models.TextField(blank=True, null=True),
        ),
    ]