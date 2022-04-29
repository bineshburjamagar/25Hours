
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from UserManagementSystem.forms import CreateUserForm, CreateOwnerForm
from django.contrib import messages
from tkinter import N
from unicodedata import name
from django.shortcuts import render, redirect


from roomManagementSystem.models import rooms, reservedDetails

from django.http import JsonResponse


from django.contrib import messages
# Create your views here.
def index(request):

    return render(request, 'index.html')

def signup(request):
    if request.method=="POST":
        user=CreateUserForm(request.POST)

        if user.is_valid():

            user.save()
            messages.success(request, 'Your account was created successfully' )
            return redirect('home')
        else :
            if user.errors:
                messages.error(request,'somthing is wronggg')
                return render(request, "SignUp.html")
    else:
        messages.success(request,'account created')
        return render(request, 'SignUp.html')
       
def ownerSignup(request):
    if request.method=="POST":
        ownerUser=CreateOwnerForm(request.POST)

        if ownerUser.is_valid():

            ownerUser.save()
            messages.success(request, 'Your account was created successfully' )
            return redirect('home')
        else :
            if ownerUser.errors:
                messages.success(request,'somthing is wronggg')
                return redirect(request, "ownerSignup.html")
    else:
        
        return render(request, 'ownerSignup.html')
           

def loginuser(request):
    if request.method == "POST":


        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request,"Login.html")

def logoutuser(request):
    logout(request)
    return render(request, 'Logout.html')

def userprofile(request):
        
        data= rooms.objects.filter(user = request.user)
        booked=reservedDetails.objects.filter(payement_status=True, user = request.user)
        context = {'data': data, 'booked':booked}
       

        return render(request, ['profile.html'], context)


def bookingDetails(request):
      data= rooms.objects.filter(user = request.user)
      booked=reservedDetails.objects.filter(payement_status=True, user_id =request.user.id)
      context = {'data': data, 'booked':booked}

      return render(request, 'bookingProfile.html', context)

   