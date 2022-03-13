from django.urls import path
from . import views

urlpatterns = [

    path('',views.index, name="home"),
    path('signup',views.signup, name="register"),
    path('login',views.loginuser, name="log"),
    path('logout',views.logoutuser, name="logout"),
    path('userprofile',views.userprofile, name="profile")
]
