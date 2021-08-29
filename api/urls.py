from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken import views as auth_views

from api import views

app_name = 'api'
urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    # path('daily_montage/', views.DailyMontageApiList.as_view(), name='daily_montage_api_list'),
    path('monter_daily', views.MonterDailyApiList.as_view(), name='monter_daily_api_list'),
    path('example/', views.DailyMontageCreateAPIView.as_view(), name='example'),
    path('list/monter', views.MonterApiList.as_view(), name='monter_api_list')
]
