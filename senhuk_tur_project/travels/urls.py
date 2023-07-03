from django.contrib import admin
from django.urls import path, include
from .views import travels, save

urlpatterns = [
    path('travels', travels),
    path('save', save, name="save"),
]