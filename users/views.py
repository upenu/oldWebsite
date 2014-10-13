from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from users.backends import CustomBackend
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.core.mail import send_mail

from users.models import *
from users.forms import *

import json

def officers(request):
    template = loader.get_template('users/officers_members.html')
    officers = UserProfile.objects.filter(user_type=3)
    positions = ['President', 'Vice President', 'Secretary', 'Treasurer',
            'Professional Development', 'Industrial Relations', 'Social', 'Publicity', 'Technology']

    for officer in officers:
        officer_profile = OfficerProfile.objects.filter(user=officer.user)
        if len(officer_profile) != 0:
            for c_officer in officer_profile:
                setattr(officer, 'position', positions[c_officer.position-1])
                setattr(officer, 'photo', officer.picture)

    context = RequestContext(request, {'users': officers, 'title': 'Officers'})
    return HttpResponse(template.render(context))

def members(request):
    template = loader.get_template('users/officers_members.html')
    members = UserProfile.objects.filter(user_type=2, approved=True)

    for member in members:
        setattr(member, 'position', 'Member')
        setattr(member, 'photo', member.picture)

    context = RequestContext(request, {'users': members, 'title': 'Members'})
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
            send_mail(user.first_name + user.last_name + " registered for a UPE account.", "You can approve this person at upe.berkeley.edu/approval_dashboard", "atlantis@upe.berkeley.edu", ["website_approval@upe.berkeley.edu"], fail_silently=True)
        else:
            print(str(user_form.errors) + " " + str(profile_form.errors))
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
            'users/register.html',
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
            user.backend = 'users.backends.CustomBackend'
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
            return render_to_response('users/login.html', 
                    context_instance=RequestContext(request,{'incorrect_log_in': incorrect_log_in}))
    else:
        return render_to_response('users/login.html', 
                context_instance=RequestContext(request,{'incorrect_log_in': incorrect_log_in}))

@login_required
def myprofile(request):
    user = request.user
    up = UserProfile.objects.get(user=user)
    resume_form = ResumeUploadForm()
    profile_pic_form = ProfilePicChangeForm()
    print(request.method)
    if request.method == 'POST':
        print(request.FILES)
        if 'resume' in request.FILES:
            resume_form = ResumeUploadForm(request.POST, request.FILES)
            print(resume_form.is_valid())
            if resume_form.is_valid():
                up.resume = request.FILES['resume']
                up.save()
        elif 'picture' in request.FILES:
            profile_pic_form = ProfilePicChangeForm(request.POST, request.FILES)
            if profile_pic_form.is_valid():
                up.picture = request.FILES['picture']
                up.save()
        elif request.POST['name'] == 'email':
            user.email = request.POST['value']
            user.save()
        elif request.POST['name'] == 'github':
            up.github = request.POST['value']
            up.save()
        elif request.POST['name'] == 'linkedin':
            up.linkedin = request.POST['value']
            up.save()
        elif request.POST['name'] == 'personal_website':
            up.personal_website = request.POST['value']
            up.save()
        elif request.POST['name'] == 'name':
            name = request.POST['value']
            p = re.compile('([a-zA-Z]+)\\s+([a-zA-Z]+)')
            m = p.match(name)
            user.first_name = m.group(1)
            user.last_name = m.group(2)
            user.save()
        elif request.POST['name'] == 'year_joined':
            up.year_joined = request.POST['value']
            up.save()
        elif request.POST['name'] == 'grad_year':
            up.grad_year = request.POST['value']
            up.save()
    return render_to_response('users/profile.html', 
            context_instance=RequestContext(request,{'up': up, 'resume_upload': resume_form, 'profile_pic': profile_pic_form}))


@user_passes_test(lambda u: UserProfile.objects.get(user=u).approved == True, login_url='/login/')
def approve_user(request, user_id):
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)
    user_profile.approved = True
    user_profile.save()
    message_text = "Hi " + user.first_name + ",\n\n Your UPE account has been approved. You can now login to our website at upe.berkeley.edu\n\n Thanks,\nUPE"
    send_mail("Your UPE Account has been approved!", message_text, "officers@upe.cs.berkeley.edu", [user.email], fail_silently=True)
    return HttpResponse("Success")

@user_passes_test(lambda u: UserProfile.objects.get(user=u).user_type == 3, login_url='/login/')
def officer_approval_dashboard(request):
    users = User.objects.filter(userprofile__approved=False)
    return render(request, 'users/officer_approval_dashboard.html', {"users": users})


    
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

    template = loader.get_template('users/officehours.html')
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

    template = loader.get_template('users/currentofficers.html')
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
    template = loader.get_template('users/requirements.html')
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
    return render(request, 'users/requirements.html',{'form': form,})


