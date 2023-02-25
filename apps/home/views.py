# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import card_info
from .models import nation,card_info,box_info,nation_name,box_has_nation
    

itme={
        "mario":"mushroom",
        "code": 123
    }


msg ="this is a test"

data_db = card_info.objects.all()
nation_all = nation.objects.all()
card_info_test = card_info.objects.all()
bt_test = box_info.objects.all()

# card_filter = card_info.objects.all().filter(nation = 'gay_ray')

def card_inf(request,pk):
    
    inf = card_info.objects.get(card_id=pk)
    context = {'inf': inf}
    html_template = loader.get_template('home/Card&deck_info.html')
    return HttpResponse(html_template.render(context,request))




def nation_card_req(request,pk):
    na_req = nation.objects.get(id=pk)
    card_fii = card_info.objects.filter(from_nation_id = na_req,)
    context = { 'na_req' : na_req , 'card_fii' : card_fii ,'nation':nation_all}
    html_template = loader.get_template('home/Clan_page.html')
    return HttpResponse(html_template.render(context,request))

    

# @login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index','nation':nation_all}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {'message':msg,'itme': itme,'data_db':data_db,'nation':nation_all,'card_info_test':card_info_test,
               'bt_te':bt_test }
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
