from django.db import models

# Create your models here.

class rooms(models.Model):
    hotel_name = models.CharField(max_length=30)
    room_type = models.CharField(max_length=30)
    room_price = models.IntegerField(max_length=30)
    room_image = models.ImageField(upload_to='images')
    room_desc = models.CharField(max_length=30)


