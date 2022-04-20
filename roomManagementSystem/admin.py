from django.contrib import admin
from .models import rooms, reservedDetails

# Register your models here.

@admin.register(rooms)
@admin.register(reservedDetails)
class RoomAdmin(admin.ModelAdmin):
    disp_list = ['hotel_name', 'room_type', 'room_price','room_number', 'room_image', 'room_desc']
