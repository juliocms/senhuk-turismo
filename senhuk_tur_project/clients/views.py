from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Client
from django.contrib.auth.models import User

@login_required(login_url="/accounts/login")
def clients(request):
    # print(request.user.email)
    
    current_user_email = request.user.email
    client = Client.objects.filter(email=current_user_email).values_list()
    
    if client:
        
        client_user = assignment_client(client)
        # print(client_user)
       
        return render(request, "clients.html", {"client": client_user})
    else:
        return render(request, "clients.html")
    # clients = Client.objects.all()
    # print(clients)
        
  
    # return render(request, "clients.html")#, {"clients": clients})

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

def assignment_client(object):
    new_object = {
        "id": object[0][0],
        "name": object[0][1],
        "mobile": object[0][2],
        "email": object[0][3],
        "social_number": object[0][4],
        "address": object[0][5],
        "birth_date": object[0][6],
        "description": object[0][7],
        "gender": object[0][8],
        
    }
    
    return new_object
    
# [(1, 'Jean Jarre25', 31974185296, 'jarrejean25@gmail.com', 95115978741, 'Rua A, 10', 
# datetime.date(1987, 10, 22), 'Possiveis contatos joao 31 9 5554-3333', 'M')]>