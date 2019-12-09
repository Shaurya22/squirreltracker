from django.urls import path

from . import views

urlpatterns = [
        path('',views.view_all),
        path('map/',views.coordinates),
        path('<str:Unique_Squirrel_Id>/edit/',views.edit_squirrel),
        path('stats/',views.stats),
]
