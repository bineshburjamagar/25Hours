from django.db import models
from UserManagementSystem.models import User

# Create your models here.
ROOOM_TYPES=[
    ('1', 'Single'),
    ('2','Double')
]
class rooms(models.Model):
    hotel_name = models.CharField(max_length=30)
    room_type = models.CharField(max_length=30, choices=ROOOM_TYPES)
    place_name = models.CharField(max_length=30, null=True, blank=True)
    room_price = models.FloatField(max_length=30)
    room_number = models.CharField(max_length=30,null=True)
    start_date = models.CharField(max_length=30, null=True, blank=True)
    end_date = models.CharField(max_length=30, null=True, blank=True)
    room_image = models.ImageField(upload_to='')
    room_desc = models.TextField()
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)

    


