- API : Application programming interface
- We built to Add/Change/Delete model data, across multiple platforms.
- API's can also be understood as remote link to your model.

HTTP Request methods for ADD/CHANGE/DELETE ACTION
====================================================
GET, POST, PUT, PATCH, DELETE 


Response : 100-599
====================
1XX : Informational 
2XX : Success
3xx : Redirection
4XX : Client side error 
5XX : Server side 

Step 1: Install django rest framework 
===========================================
pip install djangorestframework 

Step 2: Start project and app and register rest_framework and app 
==================================================================
django-admin startproject myproject
cd myproject
python manage.py migrate 
python manage.py startapp myapp

myproject --> settings.py 

INSTALLED_APPS = [
	...
    'rest_framework',
    'myapp',
    # 'myapp.apps.MyappConfig'
]

Step 3: Create a model to host and store data
=================================================
# myproject --> myapp --> models.py

from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=120)
	author = models.CharField(max_length=120)
	def __str__(self):
		return self.title

- python manage.py makemigrations
- python manage.py migrate

Step 4: Create serializers under application
==================================================
# myproject --> myapp --> serializers.py 

from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Blog 
		fields = (
			'id',
			'url',
			'title',
			'author'
			)

Step 5: Define model viewset serializer class
===============================================
# myproject --> myapp --> views.py

from django.shortcuts import render
from .models import Blog 
from .serializers import BlogSerializer
from rest_framework import viewsets

class BlogView(viewsets.ModelViewSet):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer

Step 6: Configure url reuqest routing
=========================================
# myproject --> urls.py 

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^myapp/',include('myapp.urls')),
    url(r'^rest_framework',include('rest_framework.urls'))
]

# myproject --> myapp --> urls.py 

from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'',views.BlogView)

urlpatterns = [
    url(r'',include(router.urls))
]

Step 7: Specify permisssion classes
=======================================
- python manage.py createsuperuser 

AllowAny
IsAdminUser
IsAuthenticated
IsAuthenticatedOrReadOnly

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES' : 
    ('rest_framework.permissions.IsAuthenticatedOrReadOnly',)
}

Step 8: Run server
=========================================
- python manage.py runserver