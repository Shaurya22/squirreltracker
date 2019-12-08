from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [ 
    path('',views.index),
    path('map/',views.coordinates),
    path('add/', views.add_squirrel),
    path('stats/',views.stats),
    path('<str:Unique_Squirrel_Id>/edit/',views.edit_squirrel),
]
