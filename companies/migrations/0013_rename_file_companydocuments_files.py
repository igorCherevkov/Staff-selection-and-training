# Generated by Django 4.2.4 on 2023-11-21 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_alter_companydocuments_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydocuments',
            old_name='file',
            new_name='files',
        ),
    ]
