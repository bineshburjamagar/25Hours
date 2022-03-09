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
        user =User()

        user.fname= request.POST['first_name']
        user.lname= request.POST['last_name']
        user.email= request.POST['email']
        user.username= request.POST['Username']
        user.password= request.POST['password']
        user.save()
        messages.success(request,'Congrats, your account was created successfully' )
        return redirect('home')
    else:
        
        return render(request, 'SignUp.html')
       
        
    

def login(request):
    if request.method == "POST":
            UserDetails=User.objects.get(username=request.POST['username'])
            if UserDetails.password == request.POST['password']:
                return render(request,'index.html')
    return render(request,"Login.html")