from upe_calendar.models import Event
from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta

"""
Gets Top 3 Upcoming Events from the current date
"""
def populate_footer(request):
	curr_date = datetime.combine(date.today(), time.min)
	end_date = curr_date + timedelta(days=90)
	return {'events': Event.objects.filter(start_timestamp__range=[curr_date.timestamp(), end_date.timestamp()]).order_by('start_timestamp')[:3]}
