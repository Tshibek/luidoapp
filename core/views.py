from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from . import forms
from .models import Team, Monter, MontagePaid, DailyMontage


@login_required()
def home(request):
    return render(request, 'index.html')


@login_required()
def daily_hours(request):
    dailys = DailyMontage.objects.all()
    context = locals()
    return render(request, 'hours.html',context)


@login_required()
def montage_list(request):
    montages = MontagePaid.objects.all()
    context = locals()
    return render(request, 'montage.html',context)


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
