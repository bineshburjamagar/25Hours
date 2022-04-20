from lib2to3.pgen2 import token
from multiprocessing import context
from tabnanny import check
from venv import create
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import PhotoGallary, bookedDetails, reservedDetails
from .forms import ImageForm
from .models import rooms
import requests


from django.contrib import messages
from UserManagementSystem.models import  hotel

# Create your views here.
def addRoom(request):
    data= hotel.objects.filter(user_id = request.user.id)
    context = {'data': data}
    if request.method == "POST":
        print(request.user)
        roomId = rooms.id
        room = rooms.objects.create(
        hotel_name=request.POST["hotel_name"],
        room_type=request.POST["room_type"],
        place_name=request.POST["place_name"],
        room_price=request.POST["room_price"],
        start_date= request.POST["start_date"],
        end_date=request.POST["end_date"],
        room_number=request.POST["room_number"],
        cover_image=request.FILES["cover_image"],
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



def multiple_upload(request):
    img = PhotoGallary.objects.all()
    fm = ImageForm()
    if request.method =='POST':
        fm = ImageForm(request.POST,request.FILES)
        files = request.FILES.getlist('room_image')
        if fm.is_valid():
     
            for f in files:
             gallary = PhotoGallary(room_image=f)
             gallary.save()

            return redirect('home')

    context={'form':fm,'gallimg':img}
    print(img)
    return render(request, 'addRoom.html',context)

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

def reserved_details(request,id):
    data = reservedDetails.objects.filter(user_id = request.user.id)
    room =rooms.objects.filter(id=id)
    context = {'data': data} 
    if request.method == 'POST':
        roomId = request.POST["reserve-btn"]
        room = rooms.objects.get(id=roomId)
        reserved = reservedDetails.objects.create(
        check_in=request.POST["check_in"],
        check_out=request.POST["check_out"],
        total_price=request.POST["total_price"],
        user = request.user,
        rooms = room
         )
         
        return redirect(reverse('payment')+ "?r_id="+ str(reserved.id))


    else:
         forms = reservedDetails()

    return render(request, 'roomDetails.html', context)



def payment(request):
    #  data = reservedDetails.objects.filter(user_id = request.user).last
    #  context = {'data': data} 
     r_id = request.GET.get("r_id")
     reserved = reservedDetails.objects.get(id=r_id)
     context={
         "reserved":reserved
     }
     return render(request, 'payment.html', context)

def paymentVerify(request):
    token= request.GET.get("token")
    amount= request.GET.get("amount")
    r_id= request.GET.get("reserved_id")
    print(token,amount,r_id)

   
    url = "https://khalti.com/api/v2/payment/verify/"
    payload = {
    "token": token,
    "amount": amount
    }
    headers = {
        "Authorization": "Key test_secret_key_69b9cb09e56d4c579e6f55d857329f3d"
    }
    
    reserved_obj = reservedDetails.objects.get(id=r_id)


    response = requests.post(url, payload, headers = headers)
    resp_dict = response.json()
    print(resp_dict)
    print(response)
    if resp_dict.get("idx"):
        success = True
        reserved_obj.payement_status = True
        # bookedDetails.self_save()
        reserved_obj.save()
    else:
        success = False

    data = {
        "success": success
    }
    return JsonResponse(data)


    