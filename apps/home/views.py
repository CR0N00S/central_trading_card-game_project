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
from .models import nation,card_info
    

itme={
        "mario":"mushroom",
        "code": 123
    }


msg ="this is a test"

data_db = card_info.objects.all()
nation_test = nation.objects.all()
card_info_test = card_info.objects.all()


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {'message':msg,'itme': itme,'data_db':data_db,'nation':nation_test,'card_info_test':card_info_test}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':          
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


    # load_template = request.path.split('/')[-1]

    # if load_template == 'admin':          
    #     return HttpResponseRedirect(reverse('admin:index'))
    # context['segment'] = load_template

    # html_template = loader.get_template('home/' + load_template)
    # return HttpResponse(html_template.render(context, request))
