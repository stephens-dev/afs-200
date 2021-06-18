from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

 
urlpatterns = [
    
    path('', views.home, name="plumber-home"), 
    path('about/', views.about, name="plumber-about"),
 
]