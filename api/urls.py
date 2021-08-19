from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken import views

app_name='api'
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),

]
