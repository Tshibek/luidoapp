from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone

from . import forms
from .models import Team, Monter, MontagePaid, DailyMontage, MonterDaily


@login_required()
def home(request):
    return render(request, 'index.html')


@login_required()
def monter_data_list(request, pk, name):
    monter = MonterDaily.objects.filter(name=pk, name__name=name).all().order_by('-date')
    context = locals()
    return render(request, 'list/monter_data_list.html', context)


@login_required()
def daily_hours(request):
    dailys = DailyMontage.objects.all().order_by('-date')
    context = locals()
    return render(request, 'hours.html', context)


@login_required()
def montage_list(request):
    montages = MontagePaid.objects.all().order_by('-date')
    context = locals()
    return render(request, 'montage.html', context)


@login_required()
def montage_detail(request, pk):
    montage = MontagePaid.objects.filter(pk=pk).first()
    context = locals()
    return render(request, 'details/montage_detail.html', context)


@login_required()
def monter_list(request):
    monters = Monter.objects.all()
    context = locals()
    return render(request, 'list/monter_list.html', context)


@login_required()
def add_monter(request):
    form = forms.MonterForm(request.POST)
    context = locals()
    if request.method == "POST":
        form = forms.MonterForm(request.POST)
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('core:monter_list')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Coś poszło nie tak ;(')
    return render(request, 'forms/add_monter.html', context)


@login_required()
def team_list(request):
    teams = Team.objects.all()
    context = locals()
    return render(request, 'list/team_list.html', context)


@login_required()
def add_team(request):
    form = forms.TeamForm(request.POST)
    context = locals()
    if request.method == "POST":
        form = forms.TeamForm(request.POST)
        try:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect('core:team_list')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Ekipa o tej nazwie juz istnieje!')
    return render(request, 'forms/add_teams.html', context)


@login_required()
def add_daily_montage(request):
    if request.method == 'GET':
        form_daily = forms.DailyMontageForm(request.GET or None)
        formset = forms.MonterDailyFormset(queryset=MonterDaily.objects.none())
    if request.method == "POST":
        form_daily = forms.DailyMontageForm(request.POST)
        formset = forms.MonterDailyFormset(request.POST)
        try:
            if formset.is_valid() and form_daily.is_valid():
                daily = form_daily.save(commit=False)
                daily.user = request.user
                daily.date = timezone.localdate()
                daily.save()
                for form in formset:
                    monter = form.save(commit=False)
                    monter.daily_montage = daily
                    monter.time_start = timezone.localtime()
                    monter.date = timezone.localdate()
                    monter.save()
                return redirect('core:daily_hours')
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 'MONTAŻ DODANY, PRACOWNICY PRZYDZIELENI DO INNEJ EKIPY. SKONTAKTUJ SIE Z ADMINISTRATOREM!')
    return render(request, 'forms/daily_montage.html', {
        'form_daily': form_daily,
        'formset': formset,
    })


@login_required()
def end_daily_montage(request):
    team = DailyMontage.objects.filter(user=request.user, date=timezone.localdate()).first()
    if team:
        montage = MonterDaily.objects.filter(daily_montage=team.pk).all()
        for mon in montage:
            if mon.status == 'URLOP' or mon.status == 'L4':
                start = mon.time_start
                ax = int(start.strftime('%H')) * 60 + (int(start.strftime('%M')))
                zx = (ax + 480) / 60
                h = int(zx)
                m = (h * 60) % 60
                mon.end_time = "%d:%02d" % (h, m)
                mon.save()
                all_time = 480 / 60
                ho = int(all_time)
                mins = (ho * 60) % 60
                mon.daily_hours = "%d:%02d" % (ho, mins)
                mon.save()
            else:
                mon.end_time = timezone.localtime()
                mon.save()
                end = mon.end_time
                start = mon.time_start
                x = int(end.strftime('%H')) * 60 + (int(end.strftime('%M')))
                y = int(start.strftime('%H')) * 60 + (int(start.strftime('%M')))
                time = (x - y) / 60
                hours = int(time)
                minutes = (time * 60) % 60
                mon.daily_hours = "%d:%02d" % (hours, minutes)
                mon.save()

        return HttpResponseRedirect(reverse_lazy('core:daily_hours'))


@login_required()
def montage_paid_list(request):
    pass


@login_required()
def add_montage_paid(request):
    form = forms.MontagePaidForm(request.POST)
    context = locals()
    if request.method == 'POST':
        form = forms.MontagePaidForm(request.POST)
        try:
            if form.is_valid():
                montage = DailyMontage.objects.filter(user=request.user, date=timezone.localdate()).first()
                instance = form.save(commit=False)
                instance.montage = montage
                instance.date = timezone.localdate()
                instance.save()
                return redirect('core:team_list')
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Ekipa o tej nazwie juz istnieje!')

    return render(request, 'forms/add_montage_paid.html', context)
