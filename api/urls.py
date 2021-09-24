from django.urls import path

from rest_framework.authtoken import views as auth_views

from api import views

app_name = 'api'
urlpatterns = [
    path('api-token-auth/', auth_views.obtain_auth_token, name='api-token-auth'),
    path('lista/team',views.TeamApiList.as_view(),name='team_api_list'),
    path('lista/monter', views.MonterApiList.as_view(), name='monter_api_list'),
    path('monter_daily', views.MonterDailyApiList.as_view(), name='monter_daily_api_list'),
    path('daily', views.DailyMontageCreateAPIView.as_view(), name='daily_api_post'),

]
