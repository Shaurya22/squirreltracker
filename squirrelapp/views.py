from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . models import Squirrels
from .forms import SquirrelForm

def index(request):
    context = {
            "sightings":Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
        }
    return render(request, 'squirrelapp/index.html',context)

def coordinates(request):
    squirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": squirrels,
         }
    return render(request, 'squirrelapp/map.html', context)

def edit_squirrel(request, Unique_Squirrel_ID):
    squirrel = Squirrels.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrelapp/')
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'squirrelapp/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        #check the form data
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/squirrelapp/')
    else:
        form = SquirrelForm()
    context = {
            'form':form,
        }
    return render(request, 'squirrelapp/add.html', context)

def stats(request):
    black_count = 0
    cinnamon_count = 0
    gray_count = 0
    eating_count = 0
    juvenile_count = 0
    adult_count = 0
    running_count=0
    climbing_count = 0
    chasing_count = 0
    foraging_count = 0
    kuks_count = 0
    quaas_count = 0
    moans_count = 0
    tail_flags_count=0
    for F in Squirrels.objects.all():
        if F.Running == 'TRUE':
             running_count +=1
        else:
             pass
        if F.Climbing == 'TRUE':
             climbing_count +=1
        else:
             pass
        if F.Chasing == 'TRUE':
             chasing_count +=1
        else:
             pass
        if F.Primary_Fur_Colour == 'Black':
            black_count +=1
        elif F.Primary_Fur_Colour == 'Cinnamon':
            cinnamon_count +=1
        elif F.Primary_Fur_Colour == 'Gray':
            gray_count +=1
        else:
            pass
        if F.Foraging == 'TRUE':
             foraging_count +=1
        else:
             pass
        if F.Eating == 'TRUE':
             eating_count +=1
        else:
             pass
        if F.Age == 'Juvenile':
            juvenile_count +=1
        elif F.Age == 'Adult':
            adult_count +=1
        else:
            pass
        if F.Kuks == 'TRUE':
            kuks_count +=1
        else:
            pass
        if F.Quaas =='TRUE':
            quaas_count +=1
        else:
            pass
        if F.Moans == 'TRUE':
            moans_count +=1
        else:
            pass
        if F.Tail_flags == 'TRUE':
             tail_flags_count +=1
        else:
             pass

    details = {'Number of squirrels found eating': eating_count,
                'Number of squirrels found running':running_count,
                'Number of squirrels found climbing':climbing_count,
                'Number of squirrels found chasing':chasing_count,
                'Number of squirrels found with black fur':black_count,
                'Number of squirrels found with cinnamon fur':cinnamon_count,
                'Number of squirrels found with gray fur':gray_count,
                'Number of squirrels found foraging':foraging_count,
                'Number of squirrels found flagging tails':tail_flags_count,
                'Number of squirrels found as a juvenile':juvenile_count,
                'Number of squirrels found as a adult': adult_count,
                'Number of squirrels found making kuk sounds':kuks_count,
                'Number of squirrels found making quaas sounds':quaas_count,
                'Number of squirrels found making moan sounds': moans_count,
            }
    context = {"stats":details}
    return render(request, 'squirrelapp/stats.html', context)






