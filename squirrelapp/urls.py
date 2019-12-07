from django.contrib import admin
from django.urls import path

from tracker import views

urlpatterns = [ 
    path('',views.view_all),
    path('stats/',views.stats),
    path('map/',views.coordinates),
    path('<sqatr:Unique_Squirrel_Id>/edit/',views.edit_squirrel),
]
