# Generated by Django 4.2.4 on 2023-11-28 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0023_companyvacancy_initial_test_initialtestanswers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialtestanswers',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='initialtestanswers',
            name='question',
            field=models.TextField(),
        ),
    ]
