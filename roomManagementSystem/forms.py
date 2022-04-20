
from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from roomManagementSystem.models import rooms
from .models import  PhotoGallary, reservedDetails


class CreateRoomForm(ModelForm):
    class Meta:
        model = rooms
        fields = ['hotel_name', 'room_type','place_name', 'room_price','start_date','end_date','room_number','cover_image', 'room_desc']




class ImageForm(ModelForm):
    class Meta:
        model = PhotoGallary
        fields=['room_image']  
        label ={}
        widgets ={
            'room_image':forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True}),
        } 

class ReservedDetailsForm(ModelForm):
    class Meta:
        model = reservedDetails
        fields=['check_in','check_out','total_price']