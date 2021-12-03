from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'geotask'
urlpatterns = [
    path('', views.task, name='task'),
    path('<int:pk>', views.task_content, name='task_content'),
    path('<int:pk>/status', views.update_status_task, name='update_status_geotask'),
    path('<int:pk>/images',views.add_task_images,name='add_geotask_images'),
    path('<int:pk>/komentarz',views.add_task_comment,name='add_geotask_comment')

]
