# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class CustomCreatForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'email' , 'username' , 'first_name' ,'last_name' ,'password1' , 'password2']
        labels = { 'first_name' :  'ชื่อ' , 'last_name': 'นามสกุล'

        }

    def __init__(self,*args,**kwargs):
        super(CustomCreatForm ,self).__init__(*args,**kwargs)
        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})


class AnotherForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['phone']
        labels = {'phone': 'เบอร์โทร'}
    

class profileEdit(UserCreationForm):
    class Meta:
        model = profile
        # fields = "__all__"
        fields = ['name' ,'surname' , 'phone'  ,'address' , ]
        labels = { 'name' :  'ชื่อ' , 'surname': 'นามสกุล','phone':'เบอร์โทร', 'ที่อยู่':'address'}
        # def __init__ (self, *args, **kwargs):
        #     super(profileEdit,self).__init__(*args, **kwargs)
        #     #remove what you like...
        #     self.fields.pop ('password1')
        #     self.fields.pop ('password2')


class profileUpdate_blank_addr(UserCreationForm):
    class Meta:
        model = profile
        fields = ['address' ]
        labels = { 'address' :  'ที่อยู่'}
    
    