from django.contrib import admin
from django.urls import path, include
from .views import travels, save, delete

urlpatterns = [
    path('travels', travels),
    path('save', save, name="save"),
    path('delete/<travel_id>', delete, name="delete"),
]