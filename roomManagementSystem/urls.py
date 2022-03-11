from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('host',views.addRooms, name="addRoom"),
    path('rooms',views.rooms, name="rooms")
]