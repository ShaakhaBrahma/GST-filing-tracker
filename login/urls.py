"""gst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from . import views
app_name = 'login'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('login1/', views.login1, name='login1'),
    path('R1afill/<slug:gstin>/', views.R1afill, name='R1afill'),
    path('choice/<slug:gstin>/', views.choice, name='choice'),
    path('R2afill/<slug:gstin>', views.R2afill, name='R2afill'),
    path('B3afill/<slug:gstin>', views.B3afill, name='B3afill'),
    path('clogin/', views.clogin, name='directlogin'),
    path('status/', views.status, name='status'),


]
