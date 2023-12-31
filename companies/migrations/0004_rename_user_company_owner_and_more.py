# Generated by Django 4.2.4 on 2023-11-18 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_company_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='user',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='companyvacancy',
            name='username',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
