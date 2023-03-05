# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.home import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register

    # ADD NEW Routes HERE
    path('card/<str:pk>/',views.card_inf,name='card_inf'),
    path('nation/<str:pk>/',views.nation_card_req , name='nation_card_req'),
    path('regis_card/',views.regis_card, name= 'regis_card'),
    # path('get_cardcode' , views.get_cardcode,name= 'getcardcode'),
    path('regis_card_fill/<str:pk>/',views.get_card_info_before_regis, name= 'get_card_info_regis'),
    path('updata_sale_card/<str:pk>',views.update_sale ,name ='update_sale' ),
    path('delelte_card/<str:pk>',views.del_sale ,name ='del_sale' ),
    
    
    # Leave `Home.Urls` as last the last line
    path("", include("apps.home.urls"))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)