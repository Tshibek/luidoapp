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
from . import api
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as av

app_name = 'accounts'
urlpatterns = [
    # website url
    path('login', auth_views.LoginView.as_view(template_name='signin.html'), name='login'),
    path('profil/<str:username>', views.profile, name='profile'),
    path('logout', views.logout_view, name='logout'),

    # API URL
    path('api-token-auth/', av.obtain_auth_token, name='api-token-auth'),
    path('user/current', api.CurrentUserView.as_view(), name='current_user_api')

]
