# Generated by Django 4.2.4 on 2023-11-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_rename_file_companydocuments_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocuments',
            name='doc_title',
            field=models.CharField(max_length=50),
        ),
    ]
