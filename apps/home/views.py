# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
from .models import nation_name,card_infomation ,CardWhoWantToSale , transaction_table ,Rating
from django.shortcuts import render , redirect
from .forms import * 
from apps.authentication.models import profile
from django.db.models import Avg


# from django.core.exceptions import ObjectDoesNotExist
# import json
from django.contrib import messages
    

# data_db = card_info.objects.all()
# nation_all = nation.objects.all()
# card_info_test = card_info.objects.all()
# bt_test = box_info.objects.all()
nation_al = nation_name.objects.all()
saleAll = CardWhoWantToSale.objects.all()


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
        card_form = subMit_form(request.POST ,request.FILES)
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
        sale_filter = CardWhoWantToSale.objects.filter(card_code_id = pk).order_by('-day_created')
    except sale_filter.DoesNotExist:
        sale_filter = None
    # print(sale_filter)
    
    day_labels = []

    sale_data = []
    queryset = transaction_table.objects.filter(card_code = pk).order_by('saleDay')


    for sale_detal in queryset :
        print(sale_detal.saleDay.strftime("%d-%m-%y"))
        day_labels.append(sale_detal.saleDay.strftime("%d-%m-%y"))
        sale_data.append(sale_detal.price_detal)

    context = {'infomat': inf,'new_nation_req_all':nation_al 
               , 'sale_filter' :sale_filter ,'your_profile' : your_profile 
               ,'queryset':queryset,'day_labels':day_labels,'sale_data':sale_data ,'queryset':queryset}
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

def checkRate(request,pk):
    checkuser = pk
    user_rating = Rating.objects.filter( rateUser = pk).aggregate(Avg('rate'))
    user_history = transaction_table.objects.filter(fromSalerUser = pk).order_by('saleDay')
    ratefilter = Rating.objects.filter( rateUser = pk)
    context = {'user_rating' :user_rating ,'user_history':user_history,'checkuser':checkuser ,'ratefilter':ratefilter}
    html_template = loader.get_template('home/user_rating.html')
    return HttpResponse(html_template.render(context,request))




@login_required(login_url="/login_new/")
def del_sale(request,pk):
    find_del_sale = CardWhoWantToSale.objects.get(saleId = pk)
    if request.method == 'POST':
        find_del_sale.delete()
        return redirect('/')
    context={}
    html_template = loader.get_template('home/checking_page.html')
    return HttpResponse(html_template.render(context,request))

@login_required(login_url="/login_new/")
def saleConfirm(request,pk):
    buy_form = transaction_submit()
    saleSearch = CardWhoWantToSale.objects.get(saleId = pk)
    what_price = saleSearch.sale_price
    from_user =  saleSearch.userNameWhoWantSale
    to_user = request.user.username
    what_card = saleSearch.card_code_id
    buyer_addr = request.user.profile.address
    phone_num = request.user.profile.phone
    price_update = card_infomation.objects.get(card_code = what_card)
    firstname = request.user.profile.name
    surname = request.user.profile.surname
    # print('test', what_price)
    # print('ggez' , price_update.price_average)
    # if(phone_num == None or buyer_addr is exit or firstname is exit or surname is exit):
    #     print('firstname =', request.user.profile.name)
    #     print('phone =',phone_num)
    #     print('addr = ', buyer_addr)
    #     # print('shame')
    #     # return redirect('/')
        
    #     context={}
    #     html_template = loader.get_template('home/profile.html')
    #     return HttpResponse(html_template.render(context,request))

    # else:
    if request.method == 'POST':
        
        buy_form = transaction_submit(request.POST)
        change_avd = change_price_adv(request.POST,instance=price_update)
            # print('pass?',change_avd)
            # if buy_form.is_valid():
            #     if(phone_num == None or buyer_addr is exit or firstname is exit or surname is exit):
            #         print('firstname =', request.user.profile.name)
            #         print('phone =',phone_num)
            #         print('addr = ', buyer_addr)
            #         print('shame')
            #     else:    
            #         print('out')
        buy=buy_form.save(commit=False)
        adv =change_avd.save(commit=False)
        buy.fromSalerUser = from_user
        buy.toBuyerUser = to_user
        buy.buyerAddr = buyer_addr
        buy.buyerPhone = phone_num
        buy.card_code = what_card
        buy.price_detal= what_price
        adv.price_average = what_price
            # print('ez')
        buy_form.save()
        adv.save()
        saleSearch.delete()
        return redirect('/')
    
    context={}
    html_template = loader.get_template('home/checking_page.html')
    return HttpResponse(html_template.render(context,request))


def saleHistory(request):

    current_user = request.user.username
    sale_his = CardWhoWantToSale
    transec_allTable = transaction_table
    rate_check = Rating.objects.all()
    try:
        sale_his = CardWhoWantToSale.objects.filter(userNameWhoWantSale = current_user).order_by('day_created')
    except sale_his.DoesNotExist:
        sale_his = None


    try:
        transec_allTable = transaction_table.objects.filter(toBuyerUser = current_user).order_by('-saleDay')
    except transec_allTable.DoesNotExist:
        transec_allTable = None

    queryset = transaction_table.objects.order_by('-saleDay')

    context = { 'current_user' : current_user , 'allTable' : transec_allTable 
               ,'sale_history' : sale_his , 'rate_check':rate_check}
    html_template = loader.get_template('home/salehistorypage.html')
    return HttpResponse(html_template.render(context,request))

def rateThis(request,pk):
    getTransection = transaction_table.objects.get(transaction_id = pk)
    rate_form = rate_this()
    if request.method == 'POST':
        rate_form = rate_this(request.POST)
        update_transection = transactionGoTrue(request.POST,instance = getTransection)
        print('it out')
        if rate_form.is_valid():
            rating_form = rate_form.save(commit=False)
            tran_up=update_transection.save(commit=False)
            rating_form.rating_product = getTransection
            rating_form.rateUser = getTransection.fromSalerUser
            rating_form.userWhoRateThis = request.user.username
            tran_up.is_rate = True
            tran_up.save()
            rating_form.save()
            return redirect('/')
        else:
            print('no')


    context = {'getTransection':getTransection ,'rate_form':rate_form}
    html_template = loader.get_template('home/rating.html')
    return HttpResponse(html_template.render(context,request))



def nation_card_req(request,pk):
    na_req = nation_name.objects.get(nation_nam=pk)
    card_fii = card_infomation.objects.filter(card_from_nation_id = na_req,)
    context = { 'na_req' : na_req , 'card_fii' : card_fii , 'new_nation_req_all':nation_al}
    html_template = loader.get_template('home/Clan_page.html')
    return HttpResponse(html_template.render(context,request))




# @login_required(login_url="/login/")
def index(request):
    you_rating = Rating.objects.filter( rateUser = request.user.username).aggregate(Avg('rate'))
    saleAll = CardWhoWantToSale.objects.all().order_by('-day_created')
    context = {'segment': 'index',  'new_nation_req_all':nation_al,'you_rating':you_rating , 'saleAll':saleAll}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    you_rating = Rating.objects.filter( rateUser = request.user.username).aggregate(Avg('rate'))

    context = {'new_nation_req_all':nation_al,'you_rating':you_rating}
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
