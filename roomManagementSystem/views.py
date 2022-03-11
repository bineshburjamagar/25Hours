from django.shortcuts import render

# Create your views here.
def addRooms(request):
    return render(request, 'addRoom.html')

def rooms(request):
    return render(request, 'rooms.html')

