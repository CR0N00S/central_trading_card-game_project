# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from core.settings import GITHUB_AUTH
from .models import profile
from .forms import CustomCreatForm 

def login_page(request):
        
        page = 'login'

        # if request.user.is_authenticated:
        #     return redirect('/')

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(request,'Username does not exit')
                print('Username does not exit')

            user = authenticate(request, username=username , password = password)

            if user is not None :
                login(request, user)
                return redirect('/')
            else:
                messages.error(request,'Username Or password is incorrect')
                print('Username Or password is incorrect')

        return render(request , 'home/login_page.html')

def register_page(request):
    page = 'register'
    form = CustomCreatForm()
    # phone_form = AnotherForm()

    if request.method == 'POST':
        form = CustomCreatForm(request.POST)
        # phone_form = AnotherForm(request.POST)
        if form.is_valid() :

            user =form.save()


            # phone_reg = phone_form.save(commit=False)
            # phone_reg.user = user

            # phone_reg.save()

            
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            messages.success(request,'User account was create!!')

            return redirect('home/login_page.html')
        else:
            messages.success(request,'Something not right please check again')


    context = {'page':page , 'form' :form }
    return render(request , 'home/User_register.html',context)

    

def logoutUser(request):
    logout(request)
    return redirect('/')
    

# from old template not use
def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg, "GITHUB_AUTH": GITHUB_AUTH})



def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


# from old template not use