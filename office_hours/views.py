from django.shortcuts import render
import datetime
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from office_hours.models import *

def interview_reservations(request):

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

class Format:
    def __init__(self, oh):
        self.name = oh.user
        self.image = oh.user.picture.url
        self.times = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}
        self.classes = []
        self.time_dict = oh.date_and_time.all()[0].time_dict

        classlist = []
        for klass in oh.class_name.all():
            classlist.append(klass.__str__())
        self.classes = sorted(classlist)
        for time in oh.date_and_time.all():
            self.times[time.day].append(time.hour)
        for key in self.times:
            self.times[key] = sorted(self.times[key])
        print(self.times)

    @property
    def formatted_times(self):
        string = ""
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        for key in days:
            num_of_hours = len(self.times[key])
            if num_of_hours >= 2 and num_of_hours % 2 == 0:
                string += key[:3]
                string += " "
                index = 0
                begin = 0
                end = 1
                while index < num_of_hours:
                    for entry in range(begin, end):
                        string += self.time_dict[self.times[key][begin]][:2].strip()
                        string += "-"
                        string += self.time_dict[self.times[key][end]][:2].strip()
                    index += 2
                    begin += 2
                    end += 2
                    string += ", "
        string = string.rstrip(', ')
        return string

    @property
    def tile_class(self):
        string = "tile "
        for day in self.times:
            if len(self.times[day]) >= 2:
                string += day.lower()
                string += " "
        for class_name in self.classes:
            string += class_name.lower().strip().replace(" ", "").replace("/l", "")
            string += " "
        return string.strip()

def office_hours(request):
    template = loader.get_template('office_hours/oh.html')
    objects = []
    classes = set()
    for oh in OfficeHour.objects.all():
        objects.append(Format(oh))
        for klass in oh.class_name.all():
            classes.add(klass.__str__())
    objects = sorted(objects, key=lambda x: x.name.user.last_name)
    response = {'office_hours': objects, 'classes': sorted(list(classes)), 
            'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']}
    context = RequestContext(request, response)
    return HttpResponse(template.render(context))