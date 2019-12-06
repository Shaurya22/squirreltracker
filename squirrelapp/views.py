from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import Squirrels

def index(request):
    context = {
            "Squirrel_Sightings": Squirrels.objects.all()
            }
    return render(request, 'Squirrel_Sightings/index.html',context)

