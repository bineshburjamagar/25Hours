from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.fname

class Meta:
    db_table= "hotelmanagement_user"