from django.shortcuts import render
from . import models


# Create your views here.


def todo_list(request):
    todos = models.Todo.objects.all()
    context = locals()
    return render(request, 'todo/todo.html', context)


def todo_add(request):
    context = locals()
    return render(request, 'todo/todo_add.html', context)


def todo_update(request):
    todos = models.Todo.objects.all()
    context = locals()
    return render(request, 'todo/todo.html', context)
