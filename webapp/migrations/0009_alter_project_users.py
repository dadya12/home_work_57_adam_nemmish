# Generated by Django 5.0 on 2024-01-09 04:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_project_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(default=1, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи'),
        ),
    ]