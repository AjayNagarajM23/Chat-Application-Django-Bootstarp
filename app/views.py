from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.conf import settings
from .models import Chat

# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, username + " Successfully Logged In")
            return redirect('index')
        else:
            messages.error(request, "Bad credentials ( Wrong Username Or Password )")
            return redirect('signin')

    return render(request, 'signin.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']

        if User.objects.filter(username=username):
            messages.error(request, "Username Already Exists")
            return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request, "Email Already Exists")
            return redirect('signup')
        if password != cpassword:
            messages.error(request, "Passwords don't match !")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Your account has successfully Created, Please Login To Continue")

        return render(request, 'signin.html')
    
    return render(request, 'signup.html')

def index(request): 
    chat = Chat.objects.all()
    return render(request, 'index.html', {'chat' : chat})

def addchat(request):
    if request.method == "POST":
        usr = request.user.username
        annou = request.POST['title']
        desc = request.POST['chat']
        ans_info = Chat(username=usr , title=annou, description=desc)
        ans_info.save()
        messages.success(request, "Your Chat Added")
        return redirect('index')
    
def signout(request):
    logout(request)
    messages.success(request, " Logged out Successfully ")
    return redirect('signin')