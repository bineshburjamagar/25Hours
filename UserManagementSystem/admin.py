from django.contrib import admin

# Register your models here.
from .models import User, hotelOwner
admin.site.register(User)
admin.site.register(hotelOwner)