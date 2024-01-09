from django import forms
from django.contrib.auth import get_user_model

from webapp.models import Task, Project

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {'type': forms.CheckboxSelectMultiple}

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {'users': forms.CheckboxSelectMultiple}


class ProjectUserForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['users']
        widgets = {'users': forms.CheckboxSelectMultiple}

class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=150, required=False, label='Поиск')