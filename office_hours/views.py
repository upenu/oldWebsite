from django.shortcuts import render
import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from office_hours.models import *

def office_hours(request):
    # def slot(x):
    #     result = []
    #     for day in range(1, 6):
    #         slots = OfficeHour.objects.filter(day_of_week=day, hour=x)
    #         str = ""
    #         if len(slots) == 0:
    #             str += "No scheduled officer"
    #         for i in range(len(slots)):
    #             person = User.objects.filter(username=slots[i].officer_username)[0]
    #             officer_profile = OfficerProfile.objects.filter(user=person)[0]
    #             str += "<div class=\"slot\"><div class=\"name\">" + officer_profile.name() + "</div>"
    #             str += "<div class=\"classes\">" + officer_profile.experience() + "</div></div>"
    #         result.append(str)
    #     return result

    # def group(x):
    #     result = []
    #     for i in range(10*x, 10*x+10):
    #         id = BerkeleyClass.CLASS_CHOICES[i]
    #         str = "<div class=\"group\"><div class=\"title\">" + id[1] + "</div><div class=\"tutors\">"
    #         found_class = BerkeleyClass.objects.filter(class_name=id[0])
    #         if len(found_class) > 0:
    #             tutors = found_class[0].officers.all()
    #             for j in range(len(tutors)):
    #                 str += "<div class=\"tutorname\">" + tutors[j].name() + "</div>"
    #                 str += "<div class=\"tutorschedule\">" + tutors[j].schedule() + "</div></div>"
    #         result.append(str)
    #     return result

    template = loader.get_template('office_hours/officehours.html')
    # context = RequestContext(request, {
    #     'slot_11': slot(11),
    #     'slot_12': slot(12),
    #     'slot_13': slot(13),
    #     'slot_14': slot(14),
    #     'slot_15': slot(15),
    #     'slot_16': slot(16),
    #     'slot_17': slot(17),
    #     'group_0': group(0),
    #     'group_1': group(1),
    #     'group_2': group(2),
    #     'group_3': group(3),
    #     'group_4': group(4),
    #     'group_5': group(5),
    #     })
    response = {'interviews': []}
    interviews = InterviewReservation.objects.filter(specific_date = datetime.date.today())
    if len(interviews) == 0:
        response['interviews'].append("No interviews at this time")
    for i in interviews:
        response['interviews'].append(i)

    #response = {'test' : 'hello'}
    context = RequestContext(request, response)
    # return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')
    return HttpResponse(template.render(context))


# Daniel's views.py/office_hours
# template = loader.get_template('office_hours/officehours.html')
#     ohs = OfficeHour.objects.all()

#     response = {officehours: ohs}

#     def group(x):
#         result = []
#         for i in range(10*x, 10*x+10):
#             id = BerkeleyClass.CLASS_CHOICES[i]
#             str = "<div class=\"group\"><div class=\"title\">" + id[1] + "</div><div class=\"tutors\">"
#             found_class = BerkeleyClass.objects.filter(class_name=id[0])
#             if len(found_class) > 0:
#                 tutors = found_class[0].officers.all()
#                 for j in range(len(tutors)):
#                     str += "<div class=\"tutorname\">" + tutors[j].name() + "</div>"
#                     str += "<div class=\"tutorschedule\">" + tutors[j].schedule() + "</div></div>"
#             result.append(str)
#         return result

#     context = RequestContext(request, {
#         'group_0': group(0),
#         'group_1': group(1),
#         'group_2': group(2),
#         'group_3': group(3),
#         'group_4': group(4),
#         'group_5': group(5),
#         })
