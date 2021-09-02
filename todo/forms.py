from django import forms
from . import models


class TodoForm(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ('team', 'status', 'title', 'desc', 'contact_date', 'finish_date')
