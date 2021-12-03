from django import forms
from .models import StatusTask
from django.forms import modelformset_factory


class StatusTaskForm(forms.ModelForm):
    class Meta:
        model = StatusTask
        fields = ('status',)
