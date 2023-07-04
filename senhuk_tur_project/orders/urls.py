from django.contrib import admin
from django.urls import path
from .views import orders, save_order, delete_order

urlpatterns = [
    path('orders', orders),
    path('save_order', save_order, name="save_order"),
    path('delete_order/<order_id>', delete_order, name="delete_order"),
]