from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.template import Context, Template
from django.forms import *
from django.core.serializers.json import DjangoJSONEncoder
import json, re
from users.models import *

from datetime import datetime

def index(request):
    template = loader.get_template('website/index.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)



    # context = RequestContext(request, { 'officers': officers })
    # return HttpResponse(template.render(context))
    return render(request, 'website/index.html', { 'officers': officers })

def oh(request):
    return render(request, 'website/oh.html', {})

def ir(request):
	return render(request, 'website/ir.html', {})

def interview(request):
	interview_slot_list = InterviewSlot.objects.all()
	now = datetime.now()
	date = datetime.day
	context = {'interview_slot_list': interview_slot_list, 'day': now.strftime("%A"), 'date': date}
	return render(request, 'website/interview.html', context)

def book_interview(request, slot_id):
	slot = get_object_or_404(InterviewSlot, slot_id=slot_id)
	context = {'slot': slot}
	return render(request, 'website/book_interview.html', context)
