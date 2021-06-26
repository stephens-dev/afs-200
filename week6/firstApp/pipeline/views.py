# from django.shortcuts import render
from django.contrib import admin
from django.urls import path
from . import views
from django.http import HttpResponse
from .models import myreviews
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import sqlite3


db = sqlite3.connect('db.sqlite3')
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
    for entry in revlist:
        name = entry.name 
        content = entry.content
    data = {'reviews' :revlist,'title' :"reviews"}
    # return HttpResponse (name + '' + content)
    return render(request, 'pipeline/reviews.html',data)

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else: 
            messages.info(request,'Invalid username or password')
            return redirect('/login')

    else:
        return render(request,'pipeline/login.html')

def register(request):
#   return render(request,'pipeline/register.html')

    
    # print('hit')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/register')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
        else:
            messages.info(request,'password dose not match')
            return redirect('/register')
        return redirect('/login')

    else:
        return render(request,'pipeline/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
