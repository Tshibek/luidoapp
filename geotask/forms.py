from django import forms
from .models import StatusTask, CommentTask
from django.forms import modelformset_factory


class StatusTaskForm(forms.ModelForm):
    class Meta:
        model = StatusTask
        fields = ('status',)


class CommentTaskForm(forms.ModelForm):
    class Meta:
        model = CommentTask
        fields = ('comment',)


class ImagesTaskForm(forms.Form):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))