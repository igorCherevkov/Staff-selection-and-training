# Generated by Django 4.2.4 on 2023-11-28 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0026_userstests_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsersVacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.companyvacancy')),
            ],
            options={
                'unique_together': {('username', 'vacancy')},
            },
        ),
    ]
