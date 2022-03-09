
from django.contrib.auth import logout
from django.contrib.auth import login, authenticate
from hotelmanagement.forms import CreateUserForm 
from django.contrib import messages
from tkinter import N
from unicodedata import name
from django.shortcuts import render, redirect
from .models import User
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
                return render(request, "SignUp.html", {"errors": user.errors})
    else:
        
        return render(request, 'SignUp.html')
       
        

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
        return render(request, 'profile.html')
    else:

        return redirect('Login.html')
