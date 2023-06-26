from django.shortcuts import render
from .models import Client

def clients(request):
    clients = Client.objects.all()
    
    return render(request, "clients.html", {"clients": clients})

def save(request):
    new_user = Client()
    new_user.name = request.POST.get('name')
    new_user.mobile = request.POST.get('mobile')
    new_user.email = request.POST.get('email')
    new_user.social_number = request.POST.get('social_number')
    new_user.address = request.POST.get('address')
    new_user.contact_1 = request.POST.get('contact_1')
    new_user.contact_1_mobile = request.POST.get('contact_1_mobile')
    new_user.contact_2 = request.POST.get('contact_2')
    new_user.contact_2_mobile = request.POST.get('contact_2_mobile')
    new_user.gender = request.POST.get('gender')
    new_user.birth_date = request.POST.get('birth_date')
        
    # new_user.objects.create(name=new_user.name,
    #                         mobile=new_user.mobile,
    #                         email=new_user.email,
    #                         social_number=new_user.social_number,
    #                         address=new_user.address,
    #                         contact_1=new_user.contact_1,
    #                         contact_1_mobile=new_user.contact_1_mobile,
    #                         contact_2=new_user.contact_2,
    #                         contact_2_mobile=new_user.contact_2_mobile,
    #                         gender=new_user.gender,
    #                         birth_date=new_user.birth_date
    # )
    
    new_user.save()
    
    clients = Client.objects.all()
    
    return render(request, 'clients.html', {"clients": clients}) 