from django import forms
from .models import Team, Monter, MonterDaily, DailyMontage, MontagePaid
from django.forms import modelformset_factory


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('team',)


class MonterForm(forms.ModelForm):
    class Meta:
        model = Monter
        fields = ('name','type')


class DailyMontageForm(forms.ModelForm):
    class Meta:
        model = DailyMontage
        fields = ('team', 'type', 'day_montage')



MonterDailyFormset = modelformset_factory(
    MonterDaily,
    fields=('name', 'status'),
    extra=4,

)


class MontagePaidForm(forms.ModelForm):
    class Meta:
        model = MontagePaid
        fields = ('days', 'paid', 'cabinet', 'status','comment', 'build', 'cornice', 'turnbuckles', 'type_table')


class MontageFullPaid(MontagePaidForm): #extending form
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(MontagePaidForm.Meta):
        fields = MontagePaidForm.Meta.fields + ('images',)