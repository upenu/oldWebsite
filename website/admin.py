from django.contrib import admin
from website.models import *


class ClassesTakenInline(admin.TabularInline):
    model = OfficerClass
    extra = 1

class OfficerAdmin(admin.ModelAdmin):
    fields = ('user', 'position', 'photo', 'office_hours',)
    inlines = (ClassesTakenInline,)

admin.site.register(UserProfile)
admin.site.register(OfficerProfile, OfficerAdmin)
#admin.site.register(OfficeHour)
#admin.site.register(BerkeleyClass)
#admin.site.register(CandidateProfile)
#admin.site.register(Requirement)
#admin.site.register(Completion)
