from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import Squirrels

def index(request):
    context = {
            "sightings": Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
            }
    return render(request, 'squirrelapp/index.html',context)

