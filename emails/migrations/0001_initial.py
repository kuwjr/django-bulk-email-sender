# Generated by Django 4.0.1 on 2022-01-25 06:32

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField(blank=True, max_length=5000)),
                ('recipients', django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=254), blank=True, size=None)),
                ('csvFile', models.FileField(upload_to='uploads/')),
                ('activated', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
