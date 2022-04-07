from django.contrib import admin

# Register your models here.
from .models import User, hotel
admin.site.register(User)
admin.site.register(hotel)