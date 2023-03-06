# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.template import loader
from django.urls import reverse
from .models import box_info,nation_name,card_infomation ,CardWhoWantToSale
from django.shortcuts import render , redirect
from .forms import * 
from apps.authentication.models import profile

# from django.core.exceptions import ObjectDoesNotExist
# import json
from django.contrib import messages
    

# data_db = card_info.objects.all()
# nation_all = nation.objects.all()
# card_info_test = card_info.objects.all()
bt_test = box_info.objects.all()
nation_al = nation_name.objects.all()

# card_filter = card_info.objects.all().filter(nation = 'gay_ray')

@login_required(login_url="/login_new/")
def get_card_info_before_regis(request,pk):
    # print(pk)
    profile_id_add = request.user.username
    # print(profile_id_add)
    cardYouWantToSale = card_infomation.objects.get(card_code = pk)
    # print(cardYouWantToSale.card_code,cardYouWantToSale.card_from_nation)
    card_form = subMit_form()

    upper = cardYouWantToSale.price_average +(cardYouWantToSale.price_average*0.2)
    lower = cardYouWantToSale.price_average - (cardYouWantToSale.price_average*0.2)
    if request.method == 'POST':
        card_form = subMit_form(request.POST)
        if card_form.is_valid():
            card_sub = card_form.save(commit=False)
            if card_sub.sale_price > cardYouWantToSale.price_average +(cardYouWantToSale.price_average*0.2) or card_sub.sale_price < cardYouWantToSale.price_average - (cardYouWantToSale.price_average*0.2) or card_sub.sale_price <= 0  :
                messages.success(request,'****ราคาที่คุณตั้งขายต้องไม่มากว่าหรือน้อยกว่า 80% ของราคากลาง และไม่น้อยกว่า 0 ****')
            else:
                card_sub.card_code_id = cardYouWantToSale.card_code
                card_sub.cardFromNation_id = cardYouWantToSale.card_from_nation
                card_sub.userNameWhoWantSale = profile_id_add
            # print('yeet',card_sub.sale_price)
                card_sub.save()
                return redirect('/')
        else:
            print("Something not right please check again")


    context ={'card_form':card_form , 'cardYouWantToSale' :cardYouWantToSale ,'new_nation_req_all':nation_al  , 
              'upper':upper , 'lower' : lower , 'card_price_search': cardYouWantToSale.price_average }
    html_template = loader.get_template('home/card-submit-page.html')
    return HttpResponse(html_template.render(context,request))


def card_inf(request,pk):
    
    inf = card_infomation.objects.get(card_code=pk)
    sale_filter = CardWhoWantToSale
    your_profile = request.user.username
    try:
        sale_filter = CardWhoWantToSale.objects.filter(card_code_id = pk)
    except sale_filter.DoesNotExist:
        sale_filter = None
    # print(sale_filter)
    
    context = {'infomat': inf,'new_nation_req_all':nation_al , 'sale_filter' :sale_filter ,'your_profile' : your_profile}
    html_template = loader.get_template('home/Card&deck_info.html')
    return HttpResponse(html_template.render(context,request))




@login_required(login_url="/login_new/")
def update_sale(request,pk):
    
    sale_update = CardWhoWantToSale.objects.get(saleId = pk)
    # print(sale_update.card_code_id)
    card_price_search = card_infomation.objects.get(card_code = sale_update.card_code_id)
    # print(card_price_search.price_average)
    form = subMit_update_form(instance=sale_update)
    upper = card_price_search.price_average +(card_price_search.price_average*0.2)
    lower = card_price_search.price_average - (card_price_search.price_average*0.2)
    if request.method == 'POST':
        form = subMit_update_form (request.POST ,instance=sale_update)
        form.save(commit=False)
        price_check = form.cleaned_data['sale_price']
        if form.is_valid():
            
            if price_check > card_price_search.price_average +(card_price_search.price_average*0.2) or price_check < card_price_search.price_average - (card_price_search.price_average*0.2) or price_check <= 0  :
                messages.success(request,'****ราคาที่คุณตั้งขายต้องไม่มากว่าหรือน้อยกว่า 80% ของราคากลาง และไม่น้อยกว่า 0 ****')
            else:
                # print('save!!!')
                form.save()
                return redirect('/')
    context={'form' : form , 'upper' : upper , 'lower' : lower , 'card_price_search': card_price_search.price_average }
    html_template = loader.get_template('home/card-submit-page.html')
    return HttpResponse(html_template.render(context,request))


@login_required(login_url="/login_new/")
def del_sale(request,pk):
    find_del_sale = CardWhoWantToSale.objects.get(saleId = pk)
    if request.method == 'POST':
        find_del_sale.delete()
        return redirect('/')
    context={}
    html_template = loader.get_template('home/card-submit-page.html')
    return HttpResponse(html_template.render(context,request))


def saleConfirm(request,pk):
    form = transaction_submit()
    saleSearch = CardWhoWantToSale.objects.get(saleId = pk)
    from_user =  saleSearch.userNameWhoWantSale
    to_user = request.user.username
    what_card = saleSearch.card_code_id
    buyer_addr = request.user.profile.address
    phone_num = request.user.profile.phone
    # print(saleSearch)
    print(from_user)
    print(to_user)

    # print(form.fromSalerUser)
    if request.method == 'POST':
        
        form = transaction_submit(request.POST)
        
        # print(form.fromSalerUser)

        # print('yeet')
        # print(form.fromSalerUser)
        if form.is_valid():
            form.save(commit=False)
            
            form.fromSalerUser = from_user
            form.toBuyerUser = to_user
            form.buyerAddr = buyer_addr
            form.buyerPhone = phone_num
            form.card_code = what_card
            print(form)
            print('ez')
            form.save()
    
    context={'buy_form': form}
    html_template = loader.get_template('home/card-submit-page.html')
    return HttpResponse(html_template.render(context,request))



def nation_card_req(request,pk):
    na_req = nation_name.objects.get(nation_nam=pk)
    card_fii = card_infomation.objects.filter(card_from_nation_id = na_req,)
    context = { 'na_req' : na_req , 'card_fii' : card_fii , 'new_nation_req_all':nation_al}
    html_template = loader.get_template('home/Clan_page.html')
    return HttpResponse(html_template.render(context,request))

    

# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index',  'new_nation_req_all':nation_al}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {
               'bt_te':bt_test ,}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    # try:

    #     load_template = request.path.split('/')[-1]

    #     if load_template == 'admin':          
    #         return HttpResponseRedirect(reverse('admin:index'))
    #     context['segment'] = load_template

    #     html_template = loader.get_template('home/' + load_template)
    #     return HttpResponse(html_template.render(context, request))

    # except template.TemplateDoesNotExist:

    #     html_template = loader.get_template('home/page-404.html')
    #     return HttpResponse(html_template.render(context, request))

    # except:
    #     html_template = loader.get_template('home/page-500.html')
    #     return HttpResponse(html_template.render(context, request))


    load_template = request.path.split('/')[-1]

    if load_template == 'admin':          
        return HttpResponseRedirect(reverse('admin:index'))
    context['segment'] = load_template

    html_template = loader.get_template('home/' + load_template)
    return HttpResponse(html_template.render(context, request))
