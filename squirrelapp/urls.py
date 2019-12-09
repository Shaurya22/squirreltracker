from django.urls import path
  
from . import views
app_name = 'squirrelapp'
urlpatterns = [
    path('',views.main_page, name= 'main'),
    path('map', views.get_map, name='map'),
    path('sightings/',views.get_sighting, name='sighting'),
    path('sightings/<str:Unique_squirrel_ID>/',views.edit_squirrel, name = 'edit_sighting'),
    path('sightings/add',views.add_squirrel, name = 'add_sighting'),
    path('sightings/stats', views.get_stats, name = 'stats'),
    ]
