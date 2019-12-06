from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import random
from . models import Squirrels

def index(request):
    context = {"Squirrel_Sightings": Squirrels.objects.all(), "field_names": Squirrels._meta.get_fields()}
    return render(request, 'Squirrel_Sightings/index.html',context)

def coordinates(request):
    sighting  = Squirrels.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, 'Squirrel_Sightings/map.html', context)

# Create your views here.
