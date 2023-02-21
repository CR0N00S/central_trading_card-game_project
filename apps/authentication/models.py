# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class user(models.Model):
    CUS_OR_SALE = [
        ('customer','Customer'),
        ('seller','Seller')
    ]

    user_id = models.IntegerField (primary_key=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField (max_length=60 ,unique=True)
    password = models.CharField(max_length=100 ,unique=True)
    address = models.CharField(max_length=500)
    sale = models.CharField(max_length=50,choices= CUS_OR_SALE ,default='customer')
    user_photo = models.ImageField(null=True , blank=True ,upload_to='user_icon',default="icon-van.jpg")

    