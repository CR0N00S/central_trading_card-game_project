# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import card_info,box_info,card_sale,nation,transaction,box_has_nation,box_infromation,nation_name

# Register your models here.
admin.site.register(card_info)
admin.site.register(box_info)
admin.site.register(card_sale)
admin.site.register(nation)
admin.site.register(transaction)
admin.site.register(box_has_nation)
admin.site.register(box_infromation)
admin.site.register(nation_name)