from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order
from travels.models import Travel

@login_required(login_url="/accounts/login")
def orders(request):
    
    orders = Order.objects.all()
    orders = orders[:8]
    
    travels = Travel.objects.all().order_by('-date_departure').values()
    
    return render(request, "orders.html", {"orders": orders, "travels": travels})

@login_required(login_url="/accounts/login")
def save_order(request):
    new_order = Order()
    new_travel = Travel()
    new_travel.id = request.POST.get('travel')
    new_order.travel = new_travel
    new_order.id_sender = request.user.id
    new_order.name = request.POST.get('name')
    new_order.description = request.POST.get('description')
    new_order.average_value = request.POST.get('average_value')
    new_order.approximate_weight = request.POST.get('approximate_weight')
    new_order.approximate_size = request.POST.get('approximate_size')
    new_order.recipient_data = request.POST.get('recipient_data')
        
    new_order.save()
    
    orders = Order.objects.all()
    
    return render(request, 'orders.html', {"orders": orders})

@login_required(login_url="/accounts/login")
def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
        
    orders = Order.objects.all()
    
    # return render(request, 'orders.html', {"orders": orders})
   
    return redirect("/orders/")
    # return redirect(request, 'orders.html')
