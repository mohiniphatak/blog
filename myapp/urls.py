from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.contrib.auth import authenticate,login,logout

router = routers.DefaultRouter()
router.register(r'',views.BlogView)

urlpatterns = [
    # url(r'',include(router.urls))
    url('api/',include(router.urls)),
    # url(r'^addblog/',views.addblog),
    url('showblog/',views.showblog),
    url('addblog/',views.addblog),
    url('register/',views.register, name = 'register'),
    url('login/',views.login),
]
