# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class profile(models.Model):
    CUS_OR_SALE = [
        ('customer','Customer'),
        ('seller','Seller')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=True , blank=True)
    phone = models.CharField(max_length=10, null=True , blank=True)
    email = models.EmailField (max_length=60 ,unique=True)
    address = models.CharField(max_length=500)
    sale = models.CharField(max_length=50,choices= CUS_OR_SALE ,default='customer')
    user_photo = models.ImageField(null=True , blank=True ,upload_to='user_icon',default="icon-van.jpg")
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True , editable=False)

    def __str__(self):
        return str(self.user.username)



    