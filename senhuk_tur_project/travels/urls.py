from django.contrib import admin
from django.urls import path, include
from .views import travels, save, delete_travel

urlpatterns = [
    path('travels', travels),
    path('save', save, name="save"),
    path('delete_travel/<travel_id>', delete_travel, name="delete_travel"),
]