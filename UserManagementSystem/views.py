
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from UserManagementSystem.forms import CreateUserForm, CreateOwnerForm
from django.contrib import messages
from tkinter import N
from unicodedata import name
from django.shortcuts import render, redirect

from roomManagementSystem.models import rooms
from .models import  hotelOwner
from django.http import JsonResponse
from UserManagementSystem.models import hotelOwner, User

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
                messages.success(request,'somthing is wronggg')
                return redirect(request, "SignUp.html")
    else:
        
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
    if request.user.is_authenticated:
        
        data= rooms.objects.filter(user = request.user)
        context = {'data': data}

        return render(request, 'profile.html', {'data':data})
    else:

        return redirect('Login.html')

def searchbar(request):
    if request.method=='GET':
        query = request.GET.get('query')
        if query:
           room = rooms.objects.filter(place_name=query) 
           return render(request, 'searchbar.html', {'room':room})
        else:
               print('No information to show')
               return request(request, 'searchbar.html')
