from django.urls import path

from . import views

urlpatterns = [
        path('',views.home),
        path('views/',views.index),
        path('map/',views.coordinates),
        path('add/', views.add_squirrel),
        path('views/<str:Unique_Squirrel_ID>/edit/',views.edit_squirrel),
        path('stats/',views.stats),
]
