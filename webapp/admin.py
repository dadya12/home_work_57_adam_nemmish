from django.contrib import admin
from webapp.models import Type, Status, Task

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

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type', 'created_date', 'updated_date']
    list_filter = ['id', 'status', 'type']
    search_fields = ['id', 'summary']
    fields = ['summary', 'description', 'status', 'type', 'created_date', 'updated_date']
    readonly_fields = ['created_date', 'updated_date']