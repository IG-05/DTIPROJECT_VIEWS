from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,'index.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Invalid Username/Password")
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if(password1==password2):
            my_user=User.objects.create_user(uname,email,password1)
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse("Passwords don't match")
    return render(request,'register.html')

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def loggingout(request):
    logout(request)
    return redirect('login')