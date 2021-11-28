from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils import timezone

from core.models import Team
from geotask.models import Task


def create_task(request):

    return render(request)


def task(request):
    team = Team.objects.all()
    date_today = timezone.now().date()
    geotask = Task.objects.filter(team__team=request.user.username, date=date_today).all()
    context = locals()
    return render(request, 'geotask/task.html', context)



def task_content(request,pk):
    geotask = Task.objects.get(pk=pk)
    context = locals()
    return render(request, 'geotask/task_content.html', context)


