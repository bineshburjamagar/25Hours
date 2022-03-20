from django.shortcuts import render, redirect
from roomManagementSystem.forms import CreateRoomForm
from .models import rooms

from django.contrib import messages

# Create your views here.
def addRoom(request):
    if request.method == "POST":
        room = rooms.objects.create(hotel_name=request.POST["hotel_name"],room_type=request.POST["room_type"],place_name=request.POST["place_name"],room_price=request.POST["room_price"],room_image=request.POST["room_image"],room_desc=request.POST["room_desc"])
        # messages.success(request, 'Your account was created successfully' )
        return redirect('home')
    else:
        return render(request, "addRoom.html")
            # if room.errors:
            #     messages.success(request,'somthing is wronggg')
            #     return redirect(request, "index.html", {"errors": room.errors})
        # room.save()
        # print("Kaam gardai xa")
        # return render(request, 'addRoom.html')
# def room(request):
#     return render(request, 'rooms.html')
