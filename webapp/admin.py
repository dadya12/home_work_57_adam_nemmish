from django.contrib import admin
from webapp.models import Type, Status, Task, Project

@admin.register(Type)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']
@admin.register(Status)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']


admin.site.register(Task)
admin.site.register(Project)
