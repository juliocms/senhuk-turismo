from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import Travel
from django.shortcuts import redirect

@login_required(login_url="/accounts/login")
def travels(request):
        
    if request.user.is_superuser:
        travels = Travel.objects.all().order_by('-date_departure').values()
        travels = travels[:8]
        return render(request, "travels.html", {"travels": travels})
    else:
        return redirect("/accounts/login/")


@login_required(login_url="/accounts/login")
def save(request):
    new_travel = Travel()
    new_travel.responsible_guide = request.POST.get('responsible_guide')
    new_travel.departure_destination = request.POST.get('departure_destination')
    new_travel.description = request.POST.get('description')
    new_travel.type = request.POST.get('type')
    new_travel.vehicle_plate = request.POST.get('vehicle_plate')
    new_travel.date_departure = request.POST.get('date_departure')
    new_travel.date_arrival = request.POST.get('date_arrival')
        
    new_travel.save()
    
    travels = Travel.objects.all().order_by('-date_departure').values()
    travels = travels[:8]
    
    return render(request, 'travels.html', {"travels": travels})

@login_required(login_url="/accounts/login")
def delete_travel(request, travel_id):
    travel = Travel.objects.get(pk=travel_id)
    travel.delete()
        
    travels = Travel.objects.all().order_by('-date_departure').values()
    travels = travels[:]
    
    return render(request, 'travels.html', {"travels": travels}) 