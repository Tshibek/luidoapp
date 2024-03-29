from django.contrib import admin
from django.urls import path, include, re_path
from . import views

app_name = 'stats'
urlpatterns = [
    path('stats', views.stats, name='stats'),
    path('chart/filter-options/', views.get_filter_options, name='chart-filter-options'),
    path('chart/sales/<int:year>/<str:team>/', views.get_sales_chart, name='chart-sales'),
    path('chart', views.bar_chart, name='line_chart'),
    path('chart', views.count_bar_chart, name='line_chart'),
    path("colors", views.colors, name="colors"),
    path('chartJSON', views.bar_chart_json, name='bar_chart_json'),
    path('chartCountJSON', views.count_bar_chart_json, name='bar_count_chart_json'),
]
