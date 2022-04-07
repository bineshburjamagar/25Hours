from django.forms import ModelForm
from roomManagementSystem.models import rooms

class CreateRoomForm(ModelForm):
    class Meta:
        model = rooms
        fields = ['hotel_name', 'room_type','place_name', 'room_price','start_date','end_date','room_number', 'room_image', 'room_desc']