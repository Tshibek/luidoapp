from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db import IntegrityError
from core.models import Team, MonterDaily
from geotask.forms import StatusTaskForm
from geotask.models import Task, StatusTask


def create_task(request):
    return render(request)


def task(request):
    date_today = timezone.now().date()
    geotask = Task.objects.filter(team__team=request.user.username, date=date_today).all()
    context = locals()
    return render(request, 'geotask/task.html', context)


def task_content(request, pk):
    geotask = Task.objects.get(pk=pk)
    context = locals()
    return render(request, 'geotask/task_content.html', context)


def update_status_task(request, pk):
    geotask = Task.objects.get(pk=pk)
    status = StatusTask.objects.get(task=geotask)
    form = StatusTaskForm(request.POST or None, instance=status)
    context = locals()
    if request.method == "POST":
        form = StatusTaskForm(request.POST or None, instance=status)
        try:
            if form.is_valid():
                form.save()
                check = form.cleaned_data['status']
                print(check)
                if check == 'W drodze':
                    monters = list(geotask.monters.all())
                    monter_daily = MonterDaily.objects.filter(geotask=geotask).exists()
                    print(monter_daily)
                    if monter_daily:
                        for a in monters:
                            print(a.pk)
                            MonterDaily.objects.create(name=a, geotask=geotask, time_start=timezone.localtime(),
                                                       date=timezone.localdate())


                    return redirect('geotask:task_content', pk=pk)
                return redirect('geotask:task_content', pk=pk)
            return redirect('geotask:task_content', pk=pk)
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Coś poszło nie tak ;(')

    return render(request, 'geotask/forms/update_status.html', context)
