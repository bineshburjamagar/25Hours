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
    
    roomDetails=rooms.objects.all()
    return render(request, 'rooms.html',{'rooms':roomDetails})


def searchbar(request):
    # if request.method=='GET':
    #     query = request.GET['query']
    #     if query:
    #        room = rooms.objects.filter(hotel_name__icontains=query) 
    #        return render(request, 'searchbar.html', {'rooms':room}, {'query':query})
    #     else:
    #            print('No information to show')
    #            return request(request, 'searchbar.html')
    query = request.GET['query']
    if query=='':
        return redirect('rm')
    else:
        room = rooms.objects.filter(hotel_name__icontains=query)
        
    context = {'query':query, 'rooms':room}
    return render (request, 'searchbar.html',context)


