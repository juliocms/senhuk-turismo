from django.contrib import admin
from django.urls import path, include
from .views import clients, save_user, delete_user

urlpatterns = [
    path('clients', clients),
    path('save_user', save_user, name="save_user"),
    path('delete_user/<user_id>', delete_user, name="delete_user"),
]