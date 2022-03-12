from django.contrib.auth.forms import UserCreationForm
from roomManagementSystem.models import rooms

class CreateRoomForm(UserCreationForm):
    class Meta:
        model = rooms
        fields = ['hotel_name', 'room_type', 'room_price', 'room_image', 'room_desc']