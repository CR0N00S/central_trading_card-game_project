# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
import uuid


from django.db.models.signals import post_save,post_delete

# Create your models here.

class profile(models.Model):
    CUS_OR_SALE = [
        ('customer','Customer'),
        ('seller','Seller')
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username = models.CharField(max_length=100, null=True , blank=True)
    name = models.CharField(max_length=100, null=True , blank=True)
    surname = models.CharField(max_length=100, null=True , blank=True)
    phone = models.CharField(max_length=10, null=True , blank=True)
    email = models.EmailField (max_length=60 ,unique=True)
    address = models.CharField(max_length=500)
    sale = models.CharField(max_length=50,choices= CUS_OR_SALE ,default='customer')
    user_photo = models.ImageField(null=True , blank=True ,upload_to='user_icon',default="icon-van.jpg")
    id = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True , editable=False)

    def __str__(self):
        return str(self.user.username)


def profileCreate(sender,instance , created , **kwargs):
    if created:
        user = instance
        pro =profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            surname = user.last_name
        )

    print('save!!')
    print(instance)
    print(created)


def del_profile (sender,instance,**kwargs):
    user = instance.user
    user.delete()
    


post_save.connect(profileCreate, sender=User)

post_delete.connect(del_profile,sender=profile)



    