# Generated by Django 4.2.4 on 2023-11-19 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_rename_user_company_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_title', models.CharField(max_length=50, unique=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='companyFiles')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
        ),
    ]
