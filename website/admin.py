from django.contrib import admin
from website.models import Officer, OfficerHour, OfficerClass, OfficeHour, BerkeleyClass

# Register your models here.

class OfficeHoursInline(admin.TabularInline):
    model = OfficerHour
    extra = 1

class ClassesTakenInline(admin.TabularInline):
    model = OfficerClass
    extra = 1

class OfficerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Identification',      {'fields': ['username', 'first_name', 'last_name', 'year_in_school']}),
        ('Contact Information', {'fields': ['email', 'phone_number']}),
        ('Authentification',    {'fields': ['password']}),
        ('Permissions',         {'fields': ['groups', 'user_permissions', 'is_staff', 'is_superuser']}),
        ('Activity',            {'fields': ['is_active', 'last_login', 'date_joined']}),
    ]
    inlines = (OfficeHoursInline, ClassesTakenInline,)

admin.site.register(Officer, OfficerAdmin)
admin.site.register(OfficeHour)
admin.site.register(BerkeleyClass)
