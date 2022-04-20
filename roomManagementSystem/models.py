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
    

class reservedDetails(models.Model):
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    rooms = models.ForeignKey(rooms,blank=True,on_delete=models.CASCADE,null=True)
    check_in = models.DateField(max_length=30)
    check_out = models.DateField(max_length=30)
    total_price =models.FloatField()
    payement_status = models.BooleanField(default=False, null=True, blank=True)
   
    def __str__(self):
        return "reservedDetails: " + str(self.id)


class bookedDetails(models.Model):
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)
    rooms = models.ForeignKey(rooms,blank=True,on_delete=models.CASCADE,null=True)
    booked = models.ForeignKey(reservedDetails,blank=True,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return "bookedDetails: " + str(self.id)
