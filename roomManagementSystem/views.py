from django.shortcuts import render, redirect
from roomManagementSystem.forms import CreateRoomForm
from .models import rooms
from django.contrib import messages

# Create your views here.
def addRoom(request):
    if request.method == "POST":
        room = CreateRoomForm(request.POST)

        if room.is_valid():
            room.save()
            messages.success(request, 'Your account was created successfully' )
            return redirect('home')
        else :
            if room.errors:
                messages.success(request,'somthing is wronggg')
                return redirect(request, "home", {"errors": room.errors})
        room.save()
    else:
        return render(request, 'addRoom.html')

def room(request):
    return render(request, 'rooms.html')
