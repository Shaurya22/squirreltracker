from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . models import Squirrels
from .forms import SquirrelForm

def index(request):
    context = {
            "sightings": Squirrels.objects.all(),"field_names":Squirrels._meta.get_fields()
            }
    return render(request, 'squirrelapp/index.html', context)

def coordinates(request):
    squirrels  = Squirrels.objects.all()[:100]
    context = {
            "squirrels": Squirrels,
         }
    return render(request, 'squirrelapp/map.html', context)

def edit_squirrel(request, Unique_Squirrel_Id):
    squirrel = Squirrels.objects.get(Unique_Squirrel_Id=Unique_Squirrel_Id)
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'squirrelapp/edit.html',context)
    else:
        form = SquirrelForm(instance=squirrel)
    context = {
            'form':form,
        }
    return render(request, 'squirrelapp/edit.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'squirrelapp/list/')
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
        if F.Running == True:
             running_count +=1
        else:
             pass
        if F.Climbing == True:
             climbing_count +=1
        else:
             pass
        if F.Chasing == True:
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
        if F.Foraging == True:
             foraging_count +=1
        else:
             pass
        if F.Eating == True:
             eating_count +=1
        else:
             pass
        if F.Age == 'Juvenile':
            juvenile_count +=1
        elif F.Age == 'Adult':
            adult_count +=1
        else:
            pass
        if F.Kuks == True:
            kuks_count +=1
        else:
            pass
        if F.Quaas == True:
            quaas_count +=1
        else:
            pass
        if F.Moans == True:
            moans_count +=1
        else:
            pass
        if F.Tail_flags == True:
             tail_flags_count +=1
        else:
             pass

    details = {'squirrels found eating': eating_count,
                'squirrels found running':running_count,
                'squirrels found climbing':climbing_count,
                'squirrels found chasing':chasing_count,
                'squirrels found with black fur':black_count,
                'squirrels found with cinnamon fur':cinnamon_count,
                'squirrels found with gray fur':gray_count,
                'squirrels found foraging':foraging_count,
                'squirrels found flagging tails':tail_flags_count,
                'squirrels found as a juvenile':juvenile_count,
                'squirrels found as a adult': adult_count,
                'squirrels found making kuk sounds':kuks_count,
                'squirrels found making quaas sounds':quaas_count,
                'squirrels found making moan sounds': moans_count,
            }
    context = {"stats":details}
    return render(request, 'squirrelapp/stats.html', context)




