from django.shortcuts import render, redirect
from django.utils import timezone

from . import models
from .forms import TodoForm


# Create your views here.


def todo_list(request):
    todos = models.Todo.objects.all()
    context = locals()
    return render(request, 'todo/todo.html', context)


def todo_add(request):
    form_todo = TodoForm(request.POST)
    if request.method == 'POST':
        form_todo = TodoForm(request.POST)
        if form_todo.is_valid():
            instance = form_todo.save(commit=False)
            instance.user = request.user
            instance.date = timezone.now()
            instance.save()
            return redirect('todo:todo_list')
        else:
            form_todo = TodoForm(request.GET)

    context = locals()
    return render(request, 'todo/todo_add.html', context)


def todo_update(request, pk):
    todos = models.Todo.objects.get(pk=pk)
    # form_history_todo = TodoHistoryForm(request.POST)
    context = locals()
    return render(request, 'todo/todo.html', context)
