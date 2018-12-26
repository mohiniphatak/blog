from django.contrib import admin
from .models import *
from .models import UserRegistration

admin.site.register(UserRegistration)

admin.site.register(Blog)



