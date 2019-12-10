from django.core.management.base import BaseCommand, CommandError
from squirrelapp.models import Squirrels
from django.http import HttpResponse

import csv
import sys

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        meta = Squirrels._meta
        fields = [m.name for m in meta.fields]
        csv_file = options['csv_file']
        
        print(csv_file)
        with open(csv_file,'w') as csvfile:
            w = csv.writer(csvfile)

            w.writerow(fields)
            for instance in Squirrels.objects.all():
                w.writerow([getattr(instance, field) for field in fields])


