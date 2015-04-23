from django.shortcuts import render
import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from office_hours.models import *

def office_hours(request):

    template = loader.get_template('office_hours/officehours.html')
    current_date = datetime.date.today()
    beginning_of_month = datetime.date(current_date.year, current_date.month, 1)
    week = datetime.timedelta(7)
    day = datetime.timedelta(1)
    week1_end = beginning_of_month + week
    week2_end = week1_end + week
    week3_end = week2_end + week
    week4_end = datetime.date(current_date.year, current_date.month + 1, 1) - day


    response = {'week1': [], 'week2': [], 'week3': [], 'week4': [], 
    'week1begindate': beginning_of_month, 'week1enddate': week1_end,
    'week2begindate': week1_end, 'week2enddate': week2_end,
    'week3begindate': week2_end, 'week3enddate': week3_end,
    'week4begindate': week3_end, 'week4enddate': week4_end,
    }
    interviews = InterviewReservation.objects.filter(specific_date__gte = current_date)
    for i in interviews:
        if i.available:
            if i.specific_date < week1_end and i.specific_date >= current_date:
                response['week1'].append(i)
            elif i.specific_date >= week1_end and i.specific_date < week2_end:
                response['week2'].append(i)
            elif i.specific_date >= week2_end and i.specific_date < week3_end:
                response['week3'].append(i)
            elif i.specific_date >= week3_end and i.specific_date <= week4_end:
                response['week4'].append(i)
    context = RequestContext(request, response)
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
