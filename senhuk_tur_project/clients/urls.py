from django.contrib import admin
from django.urls import path, include
from .views import clients, save

urlpatterns = [
    path('clients', clients),
    path('save', save, name="save"),
]