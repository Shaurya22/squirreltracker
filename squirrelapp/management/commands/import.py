import csv
import datetime as dt
  
from django.core.management.base import BaseCommand

from squirrelapp.models import Squirrels
from django.conf import settings

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
        
        for item in data:       
             F = Squirrels(
                Unique_Squirrel_ID = item['Unique Squirrel ID'],
                Latitude = item['X'],
                Longitude = item['Y'],
                Shift = item['Shift'],
                Date = dt.datetime.strptime(item['Date'].strip(),'%m%d%Y').date(),
                Age = item['Age'],
                Primary_Fur_Colour = item['Primary Fur Color'],
                Location = item['Location'], 
                Specific_location = item['Specific Location'],
                Running = item['Running'],
                Chasing = item['Chasing'],
                Climbing = item['Climbing'],
                Eating = item['Eating'],
                Foraging = item['Foraging'],
                Other_Activities = item['Other Activities'],
                Kuks = item['Kuks'],
                Quaas = item['Quaas'],
                Moans = item['Moans'],
                Tail_flags = item['Tail flags'],
                Tail_twitches = item['Tail twitches'],
                Approaches = item['Approaches'],
                Indifferent = item['Indifferent'],
                Runs_from = item['Runs from'],
             )
             F.save()
