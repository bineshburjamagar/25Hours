
from django.urls import re_path as url
from unicodedata import name
from django.urls import path
from . import views
namespace='hotelName'

urlpatterns = [

    path('',views.index, name="home"),
    path('signup',views.signup, name="register"),
    path('login',views.loginuser, name="log"),
    path('logout',views.logoutuser, name="logout"),
    path('userprofile',views.userprofile, name="profile"),
    path('ownerSignup',views.ownerSignup, name="ownerRegister"),
    url('', views.hotelName, name='hotelName'),
]
