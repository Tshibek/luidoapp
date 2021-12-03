from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils import timezone

from core.models import MonterDaily
from geotask.forms import StatusTaskForm, ImagesTaskForm, CommentTaskForm
from geotask.models import Task, StatusTask, TaskGallery


def task(request):
    geotask = Task.objects.filter(team__team=request.user.username, date=timezone.localdate()).all()
    context = locals()
    return render(request, 'geotask/task.html', context)


def task_content(request, pk):
    geotask = Task.objects.get(pk=pk)
    status_task = StatusTask.objects.get(task=pk)
    context = locals()
    return render(request, 'geotask/task_content.html', context)


def update_status_task(request, pk):
    geotask = Task.objects.get(pk=pk)
    print(geotask.team)
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
                    monter_daily = MonterDaily.objects.filter(date=timezone.localdate()).exists()
                    print(monter_daily)
                    if not monter_daily:
                        for a in monters:
                            print(a.pk)
                            MonterDaily.objects.create(name=a, geotask=geotask, time_start=timezone.localtime(),
                                                       date=timezone.localdate())
                    return redirect('geotask:task_content', pk=pk)
                elif check == 'Wykonana' or check == 'Niewykonana':
                    monter_daily = MonterDaily.objects.filter(geotask__team=geotask.team).all()
                    for mon in monter_daily:
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

                return redirect('geotask:task_content', pk=pk)
            return redirect('geotask:task_content', pk=pk)
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Coś poszło nie tak ;(')

    return render(request, 'geotask/forms/update_status.html', context)


def add_task_images(request,pk):
    geotask = Task.objects.get(pk=pk)
    form = ImagesTaskForm()
    context = locals()
    if request.method == 'POST':
        form = ImagesTaskForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        try:
            if form.is_valid():
                form = ImagesTaskForm(request.POST or None, request.FILES or None)
                files = request.FILES.getlist('images')
                for f in files:
                    TaskGallery.objects.create(task=geotask, user_id=request.user.pk, images=f)
            return redirect('geotask:task_content', pk=pk)
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Nie udało sie dodać zdjec!')
    return render(request, 'geotask/forms/add_task_image.html', context)


def add_task_comment(request, pk):
    geotask = Task.objects.get(pk=pk)
    form = CommentTaskForm()
    context = locals()
    if request.method == "POST":
        form = CommentTaskForm(request.POST)
        try:
            if form.is_valid():
                comment = form.save(commit=False)
                comment.task = geotask
                comment.save()
        except IntegrityError:
            messages.add_message(request, messages.ERROR, 'Komentarz został juz dodany dla tego montażu!')
        return redirect('geotask:task_content', pk=pk)

    return render(request, 'geotask/forms/add_task_comment.html',context)
