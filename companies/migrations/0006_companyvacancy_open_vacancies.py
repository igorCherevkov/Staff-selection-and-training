# Generated by Django 4.2.4 on 2023-11-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0005_companydocuments'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyvacancy',
            name='open_vacancies',
            field=models.IntegerField(default=None),
        ),
    ]
