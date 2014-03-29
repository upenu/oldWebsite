from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from website.models import *

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
                str += "\n<div class=\"slot\">\n<div class=\"name\">"
                str += person.name()
                str += "</div>\n<div class=\"classes\">"
#                 classes = person.classes_taken
#                 str += classes
                str += "</div>\n</div>\n"
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
    })
    return HttpResponse(template.render(context))
