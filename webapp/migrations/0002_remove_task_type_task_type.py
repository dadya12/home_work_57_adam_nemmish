# Generated by Django 5.0 on 2023-12-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(related_name='tasks', to='webapp.type', verbose_name='Тип'),
        ),
    ]
