from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('signup',views.signup, name="register"),
    path('login',views.login, name="log"),
]
