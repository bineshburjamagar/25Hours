from django import forms
from django.contrib.auth.forms import UserCreationForm
from UserManagementSystem.models import User, hotel


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        
class CreateOwnerForm(UserCreationForm):
    class Meta:
      model = User
      fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
      
  

         
