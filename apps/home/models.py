# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class card_info (models.Model):
    card_id = models.IntegerField(primary_key=True)
    box_id = models.IntegerField(null=False)
    card_name = models.CharField(max_length=500)
    rarity_card = models.CharField(max_length=3)
    nation = models.CharField(max_length=500)
    eff_card = models.CharField(max_length=500)
    price_adv = models.IntegerField(null=False)
    photo = models.ImageField(null=True , blank=True ,upload_to='card_img',default="ricado_mk2.jpg")
    
    
    

class box_info(models.Model):
    box_id = models.IntegerField(primary_key=True)
    box_name = models.CharField(max_length=500)
    number_of_card = models.IntegerField(null=False)
    num_rarity_c = models.IntegerField(null=False)
    num_rarity_r = models.IntegerField(null=False)
    num_rarity_rr = models.IntegerField(null=False)
    num_rarity_rrr = models.IntegerField(null=False)
    day_add = models.DateTimeField(auto_now_add=True)

class card_sale(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=False,default=0)
    card_id = models.IntegerField(null=False,default=0)
    sale_price = models.IntegerField(null=False,default=0)
    photo_upload = models.CharField(max_length=500)

class nation(models.Model):
    nation = models.CharField(max_length=500)

class transaction(models.Model):
    card_id = models.IntegerField(null=False,default=0)
    saler_id = models.IntegerField(null=False,default=0)
    buyer_id = models.IntegerField(null=False,default=0)
    card_name = models.CharField(max_length=500)
    sale_day = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(null=False,default=0)