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
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from datetime import datetime
from datetime import timedelta
import calendar

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
"""
def interview(request):
    time_dict = {9: "9:00am - 10:00am", 10: "10:00am - 11:00am", 11: "11:00am - 12:00pm", 12: "12:00pm - 1:00pm", 13: "1:00pm - 2:00pm",
                14: "2:00pm - 3:00pm", 15: "3:00pm - 4:00pm", 16: "4:00pm - 5:00pm"}
    days_of_week = [0, 1, 2, 3, 4, 5, 6]
    start_times = {0: 9, 1: 10, 2: 11, 3: 12, 4: 13, 5: 14, 6: 15, 7: 16}
    interview_slot_list = InterviewSlot.objects.all()

    now = datetime.now()
    date = datetime.day

    current_week = _get_dates_of_week(now)
    current_week_dates = [date.strftime('%b %d, %Y') for date in current_week]

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
                slot[0].date = current_week[day]
                slot[0].save()
                imputed_start_time.append(slot[0])

        time_slot_dict[start_time] = imputed_start_time
        start_time += 1



    context = {'interview_slot_list': interview_slot_list, 'day': now.strftime("%A"), 'date': date,
    "time_dict": time_dict, "time_slot_dict": time_slot_dict, "start_times": start_times,
    "range": range(len(start_times)), "week": current_week_dates}

    return render(request, 'website/interview.html', context)
"""

def interview(request):
    return render(request, 'website/temp-interview.html', {})

def _get_dates_of_week(now):
    this_week = ['date' for i in range(7)]
    current_day = now.weekday()
    if current_day == 6:
        this_week[0] = now
        for i in range(1, 7):
            add_date = now + timedelta(days=i)
            this_week[i] = add_date
    else:
        num_things_before = current_day + 1
        num_things_after = 5 - current_day
        sunday = now - timedelta(days=current_day + 1)
        this_week[0] = sunday

        for i in range(0, current_day):
            diff = current_day - i
            add_date = now - timedelta(days=diff)
            this_week[i + 1] = add_date
        for j in range(current_day + 1, 7):
            diff = j - current_day - 1
            add_date = now + timedelta(days=diff)
            this_week[j] = add_date
    return this_week

def book_interview(request, slot_id):
    all_slots = InterviewSlot.objects.all()
    for slot in all_slots:
        if slot.slot_id == slot_id:
            context = {'time_slot': slot}
            break
    return render_to_response('website/book_interview.html', RequestContext(request, context))

def confirm_interview(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')

        all_slots = InterviewSlot.objects.all()
        num_student_has = len(all_slots.filter(student=name))
        if num_student_has < 4 and _validate_name(name) and _validate_berkeley_email(email):
            booked_slot = None
            for slot in all_slots:
                if slot.get_date() == request.POST['date'] and slot.hour == int(request.POST['day_hour'][1:]):
                    booked_slot = slot
                    break
            #if booked_slot == None:
            #   return oh(request)
            booked_slot.student = request.POST['name']
            booked_slot.student_email = request.POST['email']
            booked_slot.availability = False
            booked_slot.save()
            _send_confirmation_email(booked_slot)
            return interview(request)
        else:
            return interview(request)
    else:
        return interview(request)

def _validate_name(name):
    return name is not None

def _validate_berkeley_email(email):
    try:
        validate_email(email)
    except ValidationError as e:
        return False
    else:
        if "@berkeley.edu" not in email:
            return False
    return True

def _send_confirmation_email(slot):
    student_email = slot.student_email
    interviewer = slot.officer_username
    profiles = UserProfile.objects.all()
    interviewer_email = None
    for pf in profiles:
        if pf.user.username == interviewer:
            interviewer_email = pf.user.email
    if interviewer_email is None:
        print('oops')
        return
    send_mail(
        'UPE Technical Interview Confirmation',
        '{} {} has successfully booked an interview with {} {}, on {}, at {}.'.format(slot.student,
            student_email, interviewer, interviewer_email, slot.date, slot.hour),
        'interviews@upe.berkeley.edu',
        [interviewer_email, student_email],
        fail_silently=False,
    )

def str_to_bool(s):
    if s == None:
        return False
    if s.lower() == 'on':
        return True
    return False

def requirements(request):
    # handle form submission
    requester = UserProfile.objects.get(user=request.user)

    if requester.user_type == 3:
        if request.method == 'POST':
            gm1 = str_to_bool(request.POST.get('gm1'))
            gm2 = str_to_bool(request.POST.get('gm2'))
            gm3 = str_to_bool(request.POST.get('gm3'))
            s1 = str_to_bool(request.POST.get('s1'))
            s2 = str_to_bool(request.POST.get('s2'))
            p1 = str_to_bool(request.POST.get('p1'))
            p2 = str_to_bool(request.POST.get('p2'))
            i = str_to_bool(request.POST.get('i'))
            c = str_to_bool(request.POST.get('c'))
            oc1 = str_to_bool(request.POST.get('oc1'))
            oc2 = str_to_bool(request.POST.get('oc2'))
            candidate_username = request.POST.get('candidate')
            user = User.objects.get(username = candidate_username)
            candidate = CandidateProfile.objects.get(user = user)

            # update requirements
            if gm1 != candidate.get_gm1():
                candidate.gm1 = gm1
            if gm2 != candidate.get_gm2():
                candidate.gm2 = gm2
            if gm3 != candidate.get_gm3():
                candidate.gm3 = gm3
            if s1 != candidate.get_s1():
                candidate.s1 = s1
            if s2 != candidate.get_s2():
                candidate.s2 = s2
            if p1 != candidate.get_p1():
                candidate.p1 = p1
            if p2 != candidate.get_p2():
                candidate.p2 = p2
            if i != candidate.get_i():
                candidate.i = i
            if c != candidate.get_c():
                candidate.c = c
            if oc1 != candidate.get_oc1():
                candidate.oc1 = oc1
            if oc2 != candidate.get_oc2():
                candidate.oc2 = oc2
            candidate.save()

        candidates = []
        completion = {}
        for up in UserProfile.objects.filter(user_type=1):
            cp = CandidateProfile.objects.get(user=up.user)
            reqs = {}
            if cp.get_gm1():
                reqs['gm1'] = True
            else:
                reqs['gm1'] = False
            if cp.get_gm2():
                reqs['gm2'] = True
            else:
                reqs['gm2'] = False
            if cp.get_gm3():
                reqs['gm3'] = True
            else:
                reqs['gm3'] = False
            if cp.get_s1():
                reqs['s1'] = True
            else:
                reqs['s1'] = False
            if cp.get_s2():
                reqs['s2'] = True
            else:
                reqs['s2'] = False
            if cp.get_p1():
                reqs['p1'] = True
            else:
                reqs['p1'] = False
            if cp.get_p2():
                reqs['p2'] = True
            else:
                reqs['p2'] = False
            if cp.get_i():
                reqs['i'] = True
            else:
                reqs['i'] = False
            if cp.get_c():
                reqs['c'] = True
            else:
                reqs['c'] = False
            if cp.get_oc1():
                reqs['oc1'] = True
            else:
                reqs['oc1'] = False
            if cp.get_oc2():
                reqs['oc2'] = True
            else:
                reqs['oc2'] = False

            completion[cp] = reqs
            candidates.append(cp)

        return render(request, 'website/officer_requirements_view.html', {'candidates': candidates, 'requirements': completion})
    else:
        cp = CandidateProfile.objects.get(user=request.user)
        gm1color = 'red'
        if cp.get_gm1():
            gm1color = 'green'
        gm2color = 'red'
        if cp.get_gm2():
            gm2color = 'green'
        gm3color = 'red'
        if cp.get_gm3():
            gm3color = 'green'
        s1color = 'red'
        if cp.get_s1():
            s1color = 'green'
        s2color = 'red'
        if cp.get_s2():
            s2color = 'green'
        p1color = 'red'
        if cp.get_p1():
            p1color = 'green'
        p2color = 'red'
        if cp.get_p2():
            p2color = 'green'
        icolor = 'red'
        if cp.get_i():
            icolor = 'green'
        ccolor = 'red'
        if cp.get_c():
            ccolor = 'green'
        oc1color = 'red'
        if cp.get_oc1():
            oc1color = 'green'
        oc2color = 'red'
        if cp.get_oc2():
            oc2color = 'green'
        return render(request, 'website/candidate_requirements_view.html', {'gm1': gm1color, 'gm2': gm2color, 'gm3': gm3color, 's1': s1color, 's2': s2color, 'p1': p1color, 'p2': p2color, 'i': icolor, 'c': ccolor, 'oc1': oc1color, 'oc2': oc2color, 'first_name': request.user.first_name, 'last_name': request.user.last_name})

def verify_requirements(request):
    return render(request, 'website/officer_requirements_view.html', {})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
