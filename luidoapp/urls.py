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
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.authtoken import views
from . import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('luido_admin_site/', admin.site.urls),

    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('todo', include('todo.urls', namespace='todo')),
    path('stats/', include('stats.urls', namespace='stats')),
    path('zadania/', include('geotask.urls', namespace='geotask'))

    # re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT})
]

# handler403 = 'core.error_handler.my_custom_permission_denied_view'
# handler400 = 'core.error_handler.my_custom_bad_request_view'
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
