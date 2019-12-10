from django.urls import path

from . import views

urlpatterns = [
        path('',views.index),
        path('map/',views.coordinates),
        path('add/', views.add_squirrel),
        path('<str:Unique_Squirrel_ID>/edit/',views.edit_squirrel),
        path('stats/',views.stats),
]
