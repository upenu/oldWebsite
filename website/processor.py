from upe_calendar.models import Event
from datetime import date, timedelta

"""
Gets Top 3 Upcoming Events from the current date
"""
def populate_footer(request):
	curr_date = date.today()
	end_date = curr_date + timedelta(days=90)
	return {'events': Event.objects.filter(start_time__range=[curr_date, end_date]).order_by('start_time')[:3]}