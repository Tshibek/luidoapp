from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import UpdateView

from core.models import Team
from geotask.forms import StatusTaskForm
from geotask.models import Task, StatusTask


def create_task(request):
    return render(request)


def task(request):
    team = Team.objects.all()
    date_today = timezone.now().date()
    geotask = Task.objects.filter(team__team=request.user.username, date=date_today).all()
    context = locals()
    return render(request, 'geotask/task.html', context)


def task_content(request, pk):
    geotask = Task.objects.get(pk=pk)
    status_task = StatusTask.objects.get(task=pk)
    context = locals()
    return render(request, 'geotask/task_content.html', context)


class UpdateTaskStatus(UpdateView):
    model = StatusTask
    fields = ['status']