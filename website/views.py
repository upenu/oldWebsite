from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from website.models import *
from website.forms import *
from website.backends import CustomBackend
from django.contrib.auth import login
from django.template import Context, Template

from website.models import UserProfile

from django.forms import * 

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request, {
        })
    return HttpResponse(template.render(context))

def calendar(request):
    template = loader.get_template('website/calendar.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def officers(request):
    template = loader.get_template('website/officers_members.html')
    officers = UserProfile.objects.filter(user_type=3)
    # A list of officers with their positions
    officers_position = []
    positions = ['President', 'Vice President', 'Secretary', 'Treasurer',
    'Professional Development', 'Industrial Relations', 'Social', 'Publicity', 'Technology']

    for officer in officers:
        officer_profile = OfficerProfile.objects.filter(user=officer.user)
        if len(officer_profile) != 0:
            for c_officer in officer_profile:
                setattr(officer, 'position', positions[c_officer.position-1])
                setattr(officer, 'photo', c_officer.photo)
                officers_position.append(officer)

    context = Context({'users': officers_position, 'title': 'Officers'})
    return HttpResponse(template.render(context))

def members(request):
    template = loader.get_template('website/officers_members.html')
    members = UserProfile.objects.filter(user_type=2)
    context = Context({'users': members, 'title': 'Members'})
    return HttpResponse(template.render(context))


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print(str(user_form.errors) + " " + str(profile_form.errors))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
            'website/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    context = RequestContext(request)
    incorrect_log_in = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = CustomBackend().authenticate(username=username, password=password)
        if user is not None and user != 'unapproved':
            user.backend = 'website.backends.CustomBackend'
            login(request, user)
            logged_in = True
            template = loader.get_template('website/index.html')
            context = RequestContext(request, {
                })
            return HttpResponse(template.render(context))
        elif user == 'unapproved':
            return HttpResponse("Your account has not been approved yet.")
        else:
            incorrect_log_in = True
            return render_to_response('website/login.html', 
                    context_instance=RequestContext(request,{'incorrect_log_in': incorrect_log_in}))
    else:
        return render_to_response('website/login.html', 
                context_instance=RequestContext(request,{'incorrect_log_in': incorrect_log_in}))

@login_required
def myprofile(request):
    user = request.user
    up = UserProfile.objects.get(user=user)
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            up.resume = request.FILES['resume']
            up.save()
    else:
    	form = ResumeUploadForm()
    return render_to_response('website/profile.html', 
            context_instance=RequestContext(request,{'up': up, 'resume_upload': form}))


# STUFF FOR LATER

def officehours(request):
    def slot(x):
        result = []
        for day in range(1, 6):
            slots = OfficeHour.objects.filter(day_of_week=day, hour=x)
            str = ""
            if len(slots) == 0:
                str += "No scheduled officer"
            for i in range(len(slots)):
                person = User.objects.filter(username=slots[i].officer_username)[0]
                officer_profile = OfficerProfile.objects.filter(user=person)[0]
                str += "<div class=\"slot\"><div class=\"name\">" + officer_profile.name() + "</div>"
                str += "<div class=\"classes\">" + officer_profile.experience() + "</div></div>"
            result.append(str)
        return result

    def group(x):
        result = []
        for i in range(10*x, 10*x+10):
            id = BerkeleyClass.CLASS_CHOICES[i]
            str = "<div class=\"group\"><div class=\"title\">" + id[1] + "</div><div class=\"tutors\">"
            found_class = BerkeleyClass.objects.filter(class_name=id[0])
            if len(found_class) > 0:
                tutors = found_class[0].officers.all()
                for j in range(len(tutors)):
                    str += "<div class=\"tutorname\">" + tutors[j].name() + "</div>"
                    str += "<div class=\"tutorschedule\">" + tutors[j].schedule() + "</div></div>"
            result.append(str)
        return result

    template = loader.get_template('website/officehours.html')
    context = RequestContext(request, {
        'slot_11': slot(11),
        'slot_12': slot(12),
        'slot_13': slot(13),
        'slot_14': slot(14),
        'slot_15': slot(15),
        'slot_16': slot(16),
        'slot_17': slot(17),
        'group_0': group(0),
        'group_1': group(1),
        'group_2': group(2),
        'group_3': group(3),
        'group_4': group(4),
        'group_5': group(5),
        })
    return HttpResponse(template.render(context))

def currentofficers(request):
    def officer(x):
        result = []
        found_officers = OfficerProfile.objects.filter(position=x)
        for person in found_officers:
            str = "<div class=\"officer\"><img src=\""
            str += person.photo.url + "\"/><div class=\"officername\">"
            str += person.name() + "</div><div class=\"officerposition\">"
            str += person.positionname() + "</div><div class=\"officeremail\">"
            str += person.user.email + "</div></div>"
            result.append(str)
        return result

    template = loader.get_template('website/currentofficers.html')
    context = RequestContext(request, {
        'officer_1': officer(1),
        'officer_2': officer(2),
        'officer_3': officer(3),
        'officer_4': officer(4),
        'officer_5': officer(5),
        'officer_6': officer(6),
        'officer_7': officer(7),
        'officer_8': officer(8),
        'officer_9': officer(9),
        })
    return HttpResponse(template.render(context))

def requirements(request):
    template = loader.get_template('website/requirements.html')
    if request.method == "POST":
        form = CompletionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            can = cd['candidates']
            req = cd['requirements']
            newbie = Completion.objects.create(candidate=can, requirement=req, completed=True) 
            newbie.save()
            return HttpResponseRedirect('')
    else:
        form = CompletionForm()
    return render(request, 'website/requirements.html',{'form': form,})
