# Generated by Django 4.2.4 on 2023-11-21 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_rename_files_companydocuments_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocuments',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='companies_files'),
        ),
    ]