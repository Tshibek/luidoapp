from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'geotask'
urlpatterns = [
    path('', views.task, name='task'),
    path('<int:pk>',views.task_content, name='task_content')

]