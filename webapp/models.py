from django.db import models
from django.core.exceptions import ValidationError

class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150)

    def __str__(self):
        return self.name

def validate_summary(value):
    if len(value) <= 8:
        raise ValidationError('Ваш summary заголовок слишкм кароткий. Не менее 8 символов')

def validate_description(value):
    if 'rich forever' in value.lower():
        raise ValidationError('Недопустимое слово в описании')

class Task(models.Model):
    summary = models.CharField(verbose_name='Краткое описание', max_length=200, validators=[validate_summary])
    description = models.TextField(verbose_name='Полное описание', max_length=500, null=True, blank=True, validators=[validate_description])
    status = models.ForeignKey('webapp.Status', verbose_name='Статус', on_delete=models.RESTRICT)
    type = models.ManyToManyField('webapp.Type', related_name='tasks', verbose_name='Тип')
    project = models.ForeignKey('webapp.Project', on_delete=models.PROTECT, verbose_name='Проект')
    created_date = models.DateTimeField(verbose_name='Дата и время создания', auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name='Дата и время обновления', auto_now=True)

class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    description = models.TextField(verbose_name='Опсиание', max_length=400, )
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата конца', blank=True, null=True)

    def __str__(self):
        return self.name