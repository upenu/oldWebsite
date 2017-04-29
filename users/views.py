from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.conf import settings

from users.backends import CustomBackend
from users.forms import *
from users.models import *
from users.utils import *

from oauth2client.service_account import ServiceAccountCredentials

import json
import gspread

def officers(request):
    template = loader.get_template('users/officers.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)
    for position in OfficerPosition.positions.values():
        position.users = []

    for officer in officers:
        officer_profile_list = OfficerProfile.objects.filter(user=officer.user, term=CURRENT_SEMESTER[0])
        if len(officer_profile_list) != 0:
             OfficerPosition.positions[officer_profile_list[0].position].users.append(officer)

    context = RequestContext(request,
        {'positions': OfficerPosition.positions.values(),
        'title': 'Officers',
        'current_semester': CURRENT_SEMESTER[1],
        'logged_in': request.user.is_authenticated()})
    return HttpResponse(template.render(context))

def officers2(request):
    template = loader.get_template('users/officers2.html')
    officers = UserProfile.objects.filter(user_type=3, approved=True)
    for position in OfficerPosition.positions.values():
        position.users = []

    for officer in officers:
        officer_profile_list = OfficerProfile.objects.filter(user=officer.user, term=CURRENT_SEMESTER[0])
        if len(officer_profile_list) != 0:
             OfficerPosition.positions[officer_profile_list[0].position].users.append(officer)

    context = RequestContext(request,
        {'positions': OfficerPosition.positions.values(),
        'title': 'Officers',
        'current_semester': CURRENT_SEMESTER[1],
        'logged_in': request.user.is_authenticated()})
    return HttpResponse(template.render(context))







def members(request):
    template = loader.get_template('users/members.html')
    members = UserProfile.objects.filter(user_type=2, approved=True)

    for member in members:
        setattr(member, 'position', 'Member')
        setattr(member, 'photo', member.picture)

    context = RequestContext(request,
        {'users': members,
        'title': 'Members',
        'logged_in': request.user.is_authenticated(),
        'name_filter': '',
        'grad_yr_filter': '',
        'member_since_filter_sem': '',
        'member_since_filter_year': '',
        'none_found': False
        })
    return HttpResponse(template.render(context))

# A filtering capability on the members page that can filter UPE members by graduation year, name, or
# years of membership to make searching/browsing easier for current members and candidates who are perhaps
# trying to get a feel for the number of their peers involved in UPE.
def members_filter(request):
    template = loader.get_template('users/members.html')
    name_filter = request.POST['membername'];
    grad_yr_filter = request.POST['gradyear']
    member_since_filter = request.POST['membersince']
    if len(member_since_filter):
        member_since_split = member_since_filter.split(' ')
        # split the semester string from the year number because of how Django template variables work
        member_since_filter_sem = member_since_split[0]
        member_since_filter_year = member_since_split[1]
    else:
        member_since_filter_sem = ''
        member_since_filter_year = ''
    context = RequestContext(request,
        {'users': [],
        'title': 'Members',
        'logged_in': request.user.is_authenticated(),
        'name_filter': name_filter,
        'grad_yr_filter': grad_yr_filter,
        'member_since_filter_sem': member_since_filter_sem,
        'member_since_filter_year': member_since_filter_year,
        'none_found': True
        })
    members = UserProfile.objects.filter(user_type=2, approved=True)
    filter_members = []
    for member in members:
        if len(name_filter) and name_filter not in str(member):
            continue
        if len(grad_yr_filter) and member.grad_year != grad_yr_filter[2:]:
            continue
        if len(member_since_filter) and member.year_joined != member_since_filter[0] + member_since_filter[-2:]:
            continue
        context['none_found'] = False
        filter_members.append(member);
        setattr(member, 'position', 'Member')
        setattr(member, 'photo', member.picture)
    context['users'] = filter_members
    return HttpResponse(template.render(context))

def interest(request):
    template = loader.get_template('users/application.html')
    # members = UserProfile.objects.filter(user_type=2, approved=True)

    # for member in members:
    #     setattr(member, 'position', 'Member')
    #     setattr(member, 'photo', member.picture)

    context = RequestContext(request,{
        # {'users': members,
        # 'title': 'Members',
        'logged_in': request.user.is_authenticated()})
    return HttpResponse(template.render(context))

def alumni(request):
    template = loader.get_template('users/members.html')
    alumni = UserProfile.objects.filter(user_type=4, approved=True)

    for alum in alumni:
        setattr(alum, 'position', 'Alum')
        setattr(alum, 'photo', alum.picture)

    context = RequestContext(request,
        {'users': alumni,
        'title': 'Alumni',
        'logged_in': request.user.is_authenticated()})
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
            send_mail(user.first_name + " " + user.last_name + " registered for a UPE account.", "You can approve this person after logging in at upe.berkeley.edu/approval_dashboard", "website_approval@upe.berkeley.edu", ["website_approval@upe.berkeley.edu"], fail_silently=True)
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
    bio_form = ""
    resume_form = ResumeUploadForm()
    profile_pic_form = ProfilePicChangeForm()
    gen_req_tuple = []
    com_req_tuple = []
    """
    if up.user_type == 1:
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.DRIVE_KEYFILE_NAME, scope)
        gc = gspread.authorize(credentials)
        wks_gen = gc.open(settings.DRIVE_SHEET_NAME).sheet1
        wks_com = gc.open(settings.DRIVE_SHEET_NAME).worksheet(up.get_committee_display())
        print(user.first_name + " " + user.last_name)
        try:
            user_cell_gen = wks_gen.find(user.first_name + " " + user.last_name)
            user_cell_com = wks_com.find(user.first_name + " " + user.last_name)
        except:
            print("Error finding cell")
        else:
            # general requirements stuff
            gen_req_list = []
            for col in range(1, wks_gen.col_count+1):
                if wks_gen.cell(1, col).value != "":
                    gen_req_list.append(wks_gen.cell(1, col))
                else:
                    break

            gen_req_tuple = []
            for req in gen_req_list:
                gen_req_tuple.append((req, wks_gen.cell(user_cell_gen.row, req.col)))

            # committee requirements stuff
            com_req_list = []
            for col in range(1, wks_com.col_count+1):
                if wks_com.cell(1, col).value != "":
                    com_req_list.append(wks_com.cell(1, col))
                else:
                    break

            com_req_tuple = []
            for req in com_req_list:
                com_req_tuple.append((req, wks_com.cell(user_cell_com.row, req.col)))
    """
    if request.method == 'POST':
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
        elif request.POST['name'] == 'committee':
            user.committee = request.POST['value']
            user.save()
        elif request.POST['name'] == 'Submit bio':
            #bio_form = ChangeBioForm(request.POST)
            up.officer_profile.bio = request.POST['value']
            up.officer_profile.save()

        elif request.POST['name'] == 'Submit OHtimes':
            #bio_form = ChangeBioForm(request.POST)
            up.officer_profile.ohtime = request.POST['value']
            up.officer_profile.save()
        elif request.POST['name'] == 'Submit OHclasses':
            #bio_form = ChangeBioForm(request.POST)
            up.officer_profile.ohclasses = request.POST['value']
            up.officer_profile.save()

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
            context_instance=RequestContext(request,{ 'bio': bio_form, 'up': up, 'resume_upload': resume_form, 'profile_pic': profile_pic_form }))


@user_passes_test(lambda u: UserProfile.objects.get(user=u).user_type == 3, login_url='/login/')
def approve_user(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    user_profile.approved = True
    user_profile.save()
    message_text = "Hi " + user_profile.user.first_name + ",\n\n Your UPE account has been approved. You can now login to our website at upe.berkeley.edu\n\n Thanks,\nUPE"
    send_mail("Your UPE Account has been approved!", message_text, "officers@upe.cs.berkeley.edu", [user_profile.user.email], fail_silently=True)
    return officer_approval_dashboard(request)

@user_passes_test(lambda u: UserProfile.objects.get(user=u).user_type == 3, login_url='/login/')
def reject_user(request, user_id):
    user_profile = UserProfile.objects.get(id=user_id)
    email = user_profile.user.email
    first_name = user_profile.user.first_name
    message_text = "Hi " + first_name + ",\n\n Your UPE account registration has been denied. Please contact us if this is an error.\n\n Thanks,\nUPE"
    send_mail("Your UPE account application has been rejected!", message_text, "officers@upe.cs.berkeley.edu", [email], fail_silently=True)
    user_profile.delete()
    return officer_approval_dashboard(request)


@user_passes_test(lambda u: UserProfile.objects.get(user=u).user_type == 3, login_url='/login/')
def officer_approval_dashboard(request):
    users = User.objects.filter(userprofile__approved=False)
    user_profiles = UserProfile.objects.filter(approved=False)
    return render(request, 'users/officer_approval_dashboard.html', {"users": users, "user_profiles": user_profiles})



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
"""
@login_required
def requirements(request):
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(settings.DRIVE_KEYFILE_NAME, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(settings.DRIVE_SHEET_NAME).sheet1
    user = request.user
    up = UserProfile.objects.get(user=user)

    user_cell = wks.find(user.first_name + " " + user.last_name)

    req_list = []
    for col in range(1, wks.col_count+1):
        if wks.cell(1, col).value != "":
            req_list.append(wks.cell(1, col))
        else:
            break

    req_dict = []
    for req in req_list:
        req_dict.append((req, wks.cell(user_cell.row, req.col)))

    if request.method == 'POST':
        if request.POST['name'] == 'committee':
            user.committee = request.POST['value']
            user.save()
        elif request.POST['name'] == 'name':
            name = request.POST['value']
            p = re.compile('([a-zA-Z]+)\\s+([a-zA-Z]+)')
            m = p.match(name)
            user.first_name = m.group(1)
            user.last_name = m.group(2)
            user.save()

    return render_to_response('users/requirements.html',
            context_instance=RequestContext(request,{'req_dict': req_dict, 'up':up}))
"""

