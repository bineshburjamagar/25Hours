from email.policy import default
from django.contrib.auth.models import (UserManager, AbstractUser)
from django.db import models


# UserManager class code here
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name', 'email']

    objects=UserManager()
    def __str__(self):
        return self.email
    
    is_customer = models.BooleanField(default=True)
    is_hotelOwner = models.BooleanField(default=False)
    

# class customers(models.Model):
#       user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#       objects=UserManager()
#       def __str__(self):
#         return self.email
    
#       is_customer = models.BooleanField(default=True)
#       is_hotelOwner = models.BooleanField(default=False)
    


class hotel(models.Model):
    # USERNAME_FIELD = 'username'
    

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    hotel_name = models.CharField(max_length=20,default='')
    # REQUIRED_FIELDS = ['first_name','last_name', 'email', 'hotel_name']
    is_customer = models.BooleanField(default=True)
    is_hotelOwner = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel_name
    
  

    # def save(self, *args, **kwargs):
    #     if not self.new_field:
    #         # Setting the value of new_field with website's value
    #         self.new_field = self.hotel_name

    #     # Saving the object with the default save() function
    #     super(hotelOwner, self).save(*args, **kwargs)
 

    
    
    

  