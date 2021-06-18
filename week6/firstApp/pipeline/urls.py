from django.contrib import admin
from django.urls import path
from . import views
from django.shortcuts import render

 
urlpatterns = [
    
    path('', views.home, name="pipeline-home"), 
    path('about/', views.about, name="pipeline-about"),
 
] 
# def home (request):
#     return render(request, 'pipeline/home.html')

# def about (request):
#     return render(request, 'pipeline/about.html')