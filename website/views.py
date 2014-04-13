from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic.edit import FormView
from django.contrib import messages

from website.models import *
from website.forms import *

# Create your views here.

def index(request):
    template = loader.get_template('website/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))

def officehours(request):
    def slot(x):
        result = []
        for day in range(1, 6):
            slots = OfficeHour.objects.filter(day_of_week=day, hour=x)
            str = ""
            if len(slots) == 0:
                str += "No scheduled officer"
            for i in range(len(slots)):
                person = Officer.objects.filter(username=slots[i].officer_username)[0]
                str += "<div class=\"slot\"><div class=\"name\">" + person.name() + "</div>"
                str += "<div class=\"classes\">" + person.experience() + "</div></div>"
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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/thanks/")
    else:
        form = RegisterForm()
    return render(request, "website/register.html", {
    'form': form,
    })

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active and type(user) != Unapproved:
            login(request, user)
            return HttpResponseRedirect("/thanks/")
        else:
            # Return a 'disabled account' error message
            messages.add_message(request, messages.INFO, 'Disabled account.')
    else:
        # Return an 'invalid login' error message.
        messages.add_message(request, messages.INFO, 'invalid login.')

def register_thanks(request):
    template = loader.get_template('website/register_thanks.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))
    
