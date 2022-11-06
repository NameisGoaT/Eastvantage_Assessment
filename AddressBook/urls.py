from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    
    path('',Address),
    path('create/',PostAD),
    path('update/<int:id>/',UpdateAD),
    path('delete/<int:id>/',DeleteAD),
]
