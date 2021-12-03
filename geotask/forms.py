from django import forms

from geotask.models import StatusTask


class StatusTaskForm(forms.ModelForm):
    class Meta:
        model = StatusTask
        fields = ('status',)
