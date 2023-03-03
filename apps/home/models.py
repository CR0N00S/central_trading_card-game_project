# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""


from django.db import models
import uuid
from apps.authentication.models import profile
# from django.contrib.auth.models import User

# Create your models here.

class nation(models.Model):
    nation = models.AutoField(primary_key=True)
    nation = models.CharField(max_length=500)
    def __str__(self):
        return self.nation

class nation_name(models.Model):
    nation_nam = models.CharField(primary_key=True,max_length=255)
    nation_favicon = models.CharField(max_length=500,null=True , blank=True)
    def __str__(self):
        return self.nation_nam

class box_infromation(models.Model):
    box_code = models.CharField(primary_key=True,null=False,max_length=255)  
    box_name_n = models.CharField(max_length=500,null=False)   
    def __str__(self):
        return self.box_code+ ' '+ self.box_name_n

class box_info(models.Model):
    box_id = models.AutoField(primary_key=True)
    bt_num = models.CharField(max_length=50,null=True)
    box_name = models.CharField(max_length=500)
    number_of_card = models.IntegerField(null=False)
    num_rarity_c = models.IntegerField(null=False)
    num_rarity_r = models.IntegerField(null=False)
    num_rarity_rr = models.IntegerField(null=False)
    num_rarity_rrr = models.IntegerField(null=False)
    day_add = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.bt_num + ' '+self.box_name
    
class card_info (models.Model):
    card_id = models.AutoField(primary_key=True)
    # box_id = models.IntegerField(null=False)
    card_name = models.CharField(max_length=500)
    rarity_card = models.CharField(max_length=3)
    # nation = models.CharField(max_length=500)
    eff_card = models.CharField(max_length=500)
    price_adv = models.IntegerField(null=False)
    photo = models.ImageField(null=True , blank=True ,upload_to='card_img',default="ricado_mk2.jpg")
    from_box = models.ForeignKey(box_info,null=True ,on_delete= models.SET_NULL )
    from_nation = models.ForeignKey(nation,null=True ,on_delete= models.SET_NULL )

# class card_sale(models.Model):
#     sale_id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField(null=False,default=0)
#     card_id = models.IntegerField(null=False,default=0)
#     sale_price = models.IntegerField(null=False,default=0)
#     photo_upload = models.CharField(max_length=500)

# class transaction(models.Model):
#     transaction_id = models.AutoField(primary_key=True)
#     card_id = models.IntegerField(null=False,default=0)
#     saler_id = models.IntegerField(null=False,default=0)
#     buyer_id = models.IntegerField(null=False,default=0)
#     card_name = models.CharField(max_length=500)
#     sale_day = models.DateTimeField(auto_now_add=True)
#     price = models.IntegerField(null=False,default=0)

class box_has_nation(models.Model):
    b_h_n_id = models.AutoField(primary_key=True)
    id_box = models.ForeignKey(box_infromation,null=True ,on_delete= models.SET_NULL)
    has_nation = models.ForeignKey(nation_name,null=True ,on_delete= models.SET_NULL)
    

class card_infomation (models.Model):
    card_code = models.CharField(primary_key=True,max_length=255)
    card_name_new = models.CharField(max_length=500)
    grade = models.IntegerField(default=0)
    effect_card = models.CharField(max_length=500,null=True,default=None,blank=True)
    second_effect_card = models.CharField(max_length=500,null=True,blank=True)
    third_effect_card = models.CharField(max_length=500,null=True,blank=True)
    fourth_effect_card = models.CharField(max_length=500,null=True,blank=True)
    fifth_effect_card = models.CharField(max_length=500,null=True,blank=True)
    card_from_nation = models.ForeignKey(nation_name,null=True,on_delete= models.SET_NULL)
    price_average = models.IntegerField(null=False)
    card_photo = models.ImageField(null=True , blank=True ,upload_to='card_img',default="no_infomation.png")
    def __str__(self):
        return self.card_code +' '+self.card_name_new
    
class CardWhoWantToSale (models.Model):
    saleId = models.UUIDField(default=uuid.uuid4 , unique=True ,primary_key=True , editable=False)
    cardFromNation = models.ForeignKey(nation_name,null=True,on_delete= models.SET_NULL)
    card_code = models.ForeignKey(card_infomation,null=True,on_delete= models.SET_NULL)
    
    userWhoWantSale = models.ForeignKey(profile,null=True,on_delete= models.CASCADE)
    userNameWhoWantSale = models.CharField(max_length=100,null=True,blank=True,editable=False)


    day_created =models.DateTimeField(auto_now_add=True)
    # cardPhotoWhoWantSale = models.ImageField(null=True,upload_to='sale_photo',default="no_infomation.png")
    sale_price = models.IntegerField(null=True,default=0)
    # card_code = models.ForeignKey(card_infomation,null=True,on_delete= models.SET_NULL)