# Generated by Django 4.2.4 on 2023-11-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0016_companyvacancy_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyvacancy',
            name='experience',
            field=models.CharField(blank=True, default=None, null=True),
        ),
    ]
