from django.shortcuts import render, HttpResponse, redirect
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):    
    password = request.POST['pw']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
    print(pw_hash)
    new_user = User.objects.create(user_name=request.POST['username'], password=pw_hash, first_name=request.POST['fname'], last_name=request.POST['lname']) 
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect("/")

def login(request):
    print(request.POST)
    logged_user = User.objects.filter(email=request.POST['email'])
    return redirect('/success')

def success(request):
    return render(request, 'dashboard.html')