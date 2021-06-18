from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.home, name="pipeline-home"),
# ]

# Create your views here.
def home (request):
    return render(request, 'plumber/home.html')

def about (request):
    return render(request, 'plumber/about.html')