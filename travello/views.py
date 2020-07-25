from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The city of curruption'
    dest1.img = 'destination_1.jpg'
    dest1.price = 780

    dest2 = Destination()
    dest2.name = 'Indore' 
    dest2.desc = 'Best city in the world'
    dest2.img = 'destination_2.jpg'
    dest2.price = 1000

    dest3 = Destination()
    dest3.name = 'Bhopal'
    dest3.desc = 'Also one of the best city in the world'
    dest3.img = 'destination_3.jpg'
    dest3.price = 1000

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})
