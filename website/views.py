from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from website.models import *

# Create your views here.

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

def officehours(request):
    def slot(x):
        return [x, x+1, x+2, x+3, x+4]
    template = loader.get_template('website/officehours.html')
    context = RequestContext(request, {
        'slot_11': slot(11),
        'slot_12': slot(12),
        'slot_13': slot(13),
        'slot_14': slot(14),
        'slot_15': slot(15),
        'slot_16': slot(16),
        'slot_17': slot(17),
    })
    return HttpResponse(template.render(context))
