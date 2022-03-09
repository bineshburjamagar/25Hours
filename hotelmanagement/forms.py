from django.contrib.auth.forms import UserCreationForm
from hotelmanagement.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']