from django.db import models
from UserManagementSystem.models import User

# Create your models here.
ROOOM_TYPES=[
    ('1', 'Single'),
    ('2','Double')
]
class rooms(models.Model):
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    hotel_name = models.CharField(max_length=30)
    room_type = models.CharField(max_length=30, choices=ROOOM_TYPES)
    place_name = models.CharField(max_length=30, null=True, blank=True)
    room_price = models.FloatField(max_length=30)
    room_number = models.CharField(max_length=30,null=True)
    start_date = models.CharField(max_length=30, null=True, blank=True)
    end_date = models.CharField(max_length=30, null=True, blank=True)
    cover_image = models.ImageField(upload_to='', null=True)
    room_desc = models.TextField()
   
    
class PhotoGallary(models.Model):
    rooms = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    room_image = models.FileField(upload_to='gallaries',blank=True,null=True)
    

