from django.contrib import admin
from users.models import *

# Register your models here.
class ClassesTakenInline(admin.TabularInline):
    model = OfficerClass
    extra = 1

class OfficerAdmin(admin.ModelAdmin):
    fields = ('user', 'position', 'photo', 'office_hours',)
    inlines = (ClassesTakenInline,)

class EarlyApplicantAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'reported_gpa',)
	readonly_fields = ('first_name', 'last_name', 'email')
	fieldsets = [
		('User information', {'fields': ['user', 'first_name', 'last_name', 'email']}),
		('Application', {'fields': ['reported_gpa', 'courses_taken', 'courses_a_minus', 'courses_taking', 'uploaded_transcript', 'motivation_upe']})
	]
	def first_name(self, obj):
		return obj.user.first_name

	def last_name(self, obj):
		return obj.user.last_name
	def email(self, obj):
		return obj.user.email
admin.site.register(UserProfile)
admin.site.register(OfficerProfile, OfficerAdmin)
admin.site.register(EarlyApplicant, EarlyApplicantAdmin)