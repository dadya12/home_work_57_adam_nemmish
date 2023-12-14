from django.db import models

class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

class Task(models.Model):
    summary = models.CharField(verbose_name='Краткое описание', max_length=200)
    description = models.TextField(verbose_name='Полное описание', max_length=500, null=True, blank=True)
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', on_delete=models.RESTRICT)
    type = models.ForeignKey('webapp.Type', verbose_name='Тип', on_delete=models.RESTRICT)
    created_date = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

