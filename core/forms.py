from django import forms
from .models import Team,Monter


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team',)


class MonterForm(forms.ModelForm):
    class Meta:
        model = Monter
        fields = ('name',)
