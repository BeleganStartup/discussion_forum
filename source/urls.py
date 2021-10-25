"""source URL Configuration

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
# Python Lib
from decouple import config
# Django
from django.contrib import admin
from django.urls import path, include

ADMIN_DASHBOARD = config('ADMIN_DASHBOARD')
BROWSABLE_API = config('ADMIN_DASHBOARD')

API_VERSION = 1

urlpatterns = [
    path(f'{ADMIN_DASHBOARD}/', admin.site.urls),
    path(f'{BROWSABLE_API}/', include('rest_framework.urls')),
    path(f'api/{API_VERSION}/', include('forum.urls')),
]
