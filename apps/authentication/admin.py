# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class add_to_user(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profile'

class custom_user_admin(UserAdmin):
    inlines = (add_to_user, )


admin.site.register(profile)    
admin.site.unregister(User)
admin.site.register(User,custom_user_admin)

