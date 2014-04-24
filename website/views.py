from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from website.models import *
from website.forms import *
from website.backends import CustomBackend
from django.contrib.auth import login

#from django.utils.dateformat import Dateformat
from django.forms import * 
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

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            print("A new user has been registered.")

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(str(user_form.errors) + " " + str(profile_form.errors))

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'website/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        print("Logging in")
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = CustomBackend().authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None and user != 'unapproved':
            user.backend = 'website.backends.CustomBackend'
            # Is the account active? It could have been disabled.
            login(request, user)
            print("Login successful")
            return HttpResponse('User {0} login successful'.format(username))
        elif user == 'unapproved':
            print("Unapproved user: {0}".format(username))
            return HttpResponse("Your account has not been approved yet.")
            
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('website/login.html', {}, context)

def register_thanks(request):
    template = loader.get_template('website/register_thanks.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))
