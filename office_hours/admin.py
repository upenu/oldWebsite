from django.contrib import admin
from office_hours.models import OfficeHour, InterviewReservation, Classes, DateAndTime

# Register your models here.
admin.site.register(OfficeHour)
admin.site.register(Classes)
admin.site.register(DateAndTime)
admin.site.register(InterviewReservation)