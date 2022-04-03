from django.contrib import admin
from .models import rooms

# Register your models here.

@admin.register(rooms)
class RoomAdmin(admin.ModelAdmin):
    disp_list = ['hotel_name', 'room_type', 'room_price','room_number', 'room_image', 'room_desc']
