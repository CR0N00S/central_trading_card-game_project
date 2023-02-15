# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class card_info (models.Model):
    card_id = models.IntegerField(primary_key=True)
    box_id = models.IntegerField
    card_name = models.CharField(max_length=500)
    eff_card = models.CharField(max_length=500)
    rarity_card = models.CharField(max_length=3)
    price_adv = models.IntegerField
    photo = models.CharField(max_length=500)
    nation = models.CharField

class box_info(models.Model):
    box_id = models.IntegerField(primary_key=True)
    box_name = models.CharField(max_length=500)
    number_of_card = models.IntegerField
    num_rarity_c = models.IntegerField
    num_rarity_r = models.IntegerField
    num_rarity_rr = models.IntegerField
    num_rarity_rrr = models.IntegerField
    day_add = models.DateTimeField(auto_now_add=True)

class card_sale(models.Model):
    sale_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField
    card_id = models.IntegerField
    sale_price = models.IntegerField
    photo_upload = models.CharField(max_length=500)

class nation(models.Model):
    nation = models.CharField(max_length=500)

class transaction(models.Model):
    card_id = models.IntegerField
    saler_id = models.IntegerField
    buyer_id = models.IntegerField
    card_name = models.CharField(max_length=500)
    sale_day = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField