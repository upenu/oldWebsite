from django.shortcuts import render
from calendar import monthrange
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from upe_calendar.models import *
from datetime import date, timedelta
import json
from django.core.serializers.json import DjangoJSONEncoder


def calendar(request):
    # Import here because of circular dependency issue (http://stackoverflow.com/questions/6381225/import-issue-with-python-django)
    import datetime, calendar
    template = loader.get_template('upe_calendar/calendar.html')
    now = datetime.datetime.now()
    num_days = calendar.monthrange(now.year, now.month)[1]
    weekday = int(now.weekday())
    context = RequestContext(request, {'month': now.strftime('%B'), 'year': now.year})
    return HttpResponse(template.render(context))

"""
Returns events occuring during the current month
"""
def get_calendar_info(request):
    if request.method == 'GET':
        response = {'events': {}}
        curr_date = date.today()
        events = Event.objects.filter(start_time__month=curr_date.month, start_time__year=curr_date.year)
        for event in events:
            response['events'][event.name] = event.start_time
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')
