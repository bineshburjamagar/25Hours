from django.shortcuts import render, redirect
from roomManagementSystem.forms import CreateRoomForm
from .models import rooms

from django.contrib import messages
from UserManagementSystem.models import  hotel

# Create your views here.
def addRoom(request):
    data= hotel.objects.filter(user_id = request.user.id)
    context = {'data': data}
    if request.method == "POST":
        print(request.user)
        room = rooms.objects.create(
        hotel_name=request.POST["hotel_name"],
        room_type=request.POST["room_type"],
        place_name=request.POST["place_name"],
        room_price=request.POST["room_price"],
        start_date= request.POST["start_date"],
        end_date=request.POST["end_date"],
        room_number=request.POST["room_number"],
        room_image=request.FILES["room_image"],
        room_desc=request.POST["room_desc"],
        user = request.user
        )
        # messages.success(request, 'Your account was created successfully' )
       
        return redirect('home')
    else:
        
        return render(request, "addRoom.html",context)
            # if room.errors:
            #     messages.success(request,'somthing is wronggg')
            #     return redirect(request, "index.html", {"errors": room.errors})
        # room.save()
        # print("Kaam gardai xa")
        # return render(request, 'addRoom.html')
def room(request):
    
    allRooms=rooms.objects.all()
    return render(request, 'rooms.html',{'rooms':allRooms})


def searchbar(request):
   
    query = request.GET['query']
    if query=='':
        return redirect('rm')
    else:
        place = rooms.objects.filter(place_name__icontains=query)
        checkIn = rooms.objects.filter(start_date__icontains=query)
        checkOut = rooms.objects.filter(end_date__icontains=query)
        search=place.union(checkIn,checkOut)
    


        
    context = {'query':query, 'rooms':search}
    return render (request, 'searchbar.html',context)

def roomDetails(request,id):
    data =rooms.objects.filter(id=id)
    context= {"roomDetails": data[0]}

    return render(request,'roomDetails.html',context)

