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
	time_dict = {9: "9:00 - 10:00", 10: "10:00 - 11:00", 11: "11:00 - 12:00", 12: "12:00 - 1:00", 13: "1:00 - 2:00",
				14: "2:00 - 3:00", 15: "3:00 - 4:00", 16: "4:00 - 5:00"}
	days_of_week = [0, 1, 2, 3, 4, 5, 6]
	start_times = {0: 9, 1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
	interview_slot_list = InterviewSlot.objects.all()

	time_slot_dict = {}
	start_time = 9
	for _ in range(len(time_dict)):
		filter_start_time = interview_slot_list.filter(hour=start_time)
		imputed_start_time = []
		for day in days_of_week:
			slot = filter_start_time.filter(day_of_week=day)
			if len(slot) == 0:
				imputed_start_time.append(None)
			else:
				#There should only be one slot from this filter 
				imputed_start_time.append(slot[0])
		time_slot_dict[start_time] = imputed_start_time
		start_time += 1

	now = datetime.now()
	date = datetime.day

	context = {'interview_slot_list': interview_slot_list, 'day': now.strftime("%A"), 'date': date, 
	"time_dict": time_dict, "time_slot_dict": time_slot_dict, "start_times": start_times, 
	"range": range(len(start_times))}

	return render(request, 'website/interview.html', context)

def book_interview(request, slot_id):
	all_slots = InterviewSlot.objects.all()
	for slot in all_slots:
		if slot.slot_id == slot_id:
			context = {'slot': slot}
			break
	return render(request, 'website/book_interview.html', context)
