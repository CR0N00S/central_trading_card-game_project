# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, include
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('login_new/',views.login_page, name= 'login_form'),
    path('register_new/',views.register_page, name= 'register_form') , 
    path('logout_new/',views.logoutUser, name= 'logout_fo'),

    
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('social_login/', include('allauth.urls')),
]
