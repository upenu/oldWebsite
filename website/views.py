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
    template = loader.get_template('website/officehours.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))
