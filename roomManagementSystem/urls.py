from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [

    path('add',views.addRoom, name="addRoom"),
    path('details',views.room, name="rooms")
]