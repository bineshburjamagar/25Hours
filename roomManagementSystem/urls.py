from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path("roomAdd",views.addRoom, name="roomAdd"),
    # path('details/',views.room, name="rm")
]