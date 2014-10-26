from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from users.models import *

def index(request):
    template = loader.get_template('website/index.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)
    # context = RequestContext(request, { 'officers': officers })
    # return HttpResponse(template.render(context))
    return render(request, 'website/index.html', { "officers": officers })
