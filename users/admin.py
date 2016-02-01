from django.contrib import admin
from users.models import *

## Register your models here.
#class ClassesTakenInline(admin.TabularInline):
#    model = OfficerClass
#    extra = 1

class OfficerAdmin(admin.ModelAdmin):
    fields = ('user', 'position', 'term', 'bio')
#    inlines = (ClassesTakenInline,)

admin.site.register(UserProfile)
admin.site.register(OfficerProfile, OfficerAdmin)
