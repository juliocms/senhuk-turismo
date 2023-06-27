from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Client

@login_required(login_url="/accounts/login")
def clients(request):
    clients = Client.objects.all()
  
    return render(request, "clients.html", {"clients": clients})

@login_required(login_url="/accounts/login")
def save(request):
    new_user = Client()
    new_user.name = request.POST.get('name')
    new_user.mobile = request.POST.get('mobile')
    new_user.email = request.POST.get('email')
    new_user.social_number = request.POST.get('social_number')
    new_user.address = request.POST.get('address')
    new_user.description = request.POST.get('description')
    new_user.gender = request.POST.get('gender')
    new_user.birth_date = request.POST.get('birth_date')
        
    new_user.save()
    
    clients = Client.objects.all()
    
    return render(request, 'clientsList.html', {"clients": clients}) 