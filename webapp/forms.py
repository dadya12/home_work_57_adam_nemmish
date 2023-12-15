from django import forms
from webapp.models import Type, Status
from django.forms import widgets

class TaskForm(forms.Form):
    summary = forms.CharField(label='Summary', required=True, max_length=200)
    description = forms.CharField(label='Description', max_length=500, widget=widgets.Textarea, required=False)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label='Status', required=True)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), label='Type', required=True)