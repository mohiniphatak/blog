"""withdb URL Configuration

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
from django.urls import path, include
from withdb import views
# from django.conf.urls import url, include

urlpatterns = [
    # path('', views.login_redirect, name='login_redirect'),#to set register page as index
    path('admin/', admin.site.urls),
   
    path('',include('myapp.urls')),
    path('rest_framework',include('rest_framework.urls')),
]
