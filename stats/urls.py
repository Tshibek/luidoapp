from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'stats'
urlpatterns = [
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/sales/<int:year>/<str:team>/', views.get_sales_chart, name='chart-sales'),
]
