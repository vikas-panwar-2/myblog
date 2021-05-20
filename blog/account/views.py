from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
import math, random

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/list')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('.')

    else:
        return render(request, 'login.html')

def signout(request):
    auth.logout(request)
    return redirect('/')
    
def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register_user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email address already taken')
                return redirect('register_user')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                auth.login(request, user)
                return redirect('/list')
        else:
            messages.info(request, 'password not matching..')
            return redirect('register_user')

        return redirect('/list')

    else:    
        return render(request,'register.html')


