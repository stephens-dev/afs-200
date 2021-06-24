from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpResponse
from .models import myreviews


# urlpatterns = [
#     path('', views.home, name="pipeline-home"),
# ]

# Create your views here.
def home (request):
    return render(request, 'pipeline/home.html')

def about (request):
    return render(request, 'pipeline/about.html')

def reviews (request):
    revlist = myreviews.objects.all()
    # for entry in revlist:
    #     name = entry.name 
    #     content = entry.content
    data = {'reviews' :revlist,'title' :"reviews"}
    # return HttpResponse (name + '' + content)
    return render(request, 'pipeline/reviews.html',data)


