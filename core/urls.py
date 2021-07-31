"""luidoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),


    path('daily', views.daily_hours, name='daily_hours'),
    path('endwork',views.end_daily_montage,name="end_work"),

    path('montage', views.montage_list, name='montage_list'),
    path('montage/add', views.add_daily_montage,name='montage_post'),
    path('montage/<int:pk>', views.montage_detail,name='montage_detail'),

    path('monter', views.monter_list, name='monter_list'),
    path('monter/add', views.add_monter, name='add_monter'),
    path('monter/<int:pk>/<str:name>', views.monter_data_list, name='monter_data_list'),

    path('paid', views.montage_paid_list, name='montage_paid_list'),
    path('paid/add',views.add_montage_paid, name='montage_paid_post'),


    path('teams', views.team_list,name='team_list'),
    path('teams/add',views.add_team,name='add_team'),
]
