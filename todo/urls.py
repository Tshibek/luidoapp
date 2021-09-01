
from django.urls import path


from todo import views

app_name = 'todo'
urlpatterns = [
    path('lista', views.todo_list, name='todo_list'),
]
