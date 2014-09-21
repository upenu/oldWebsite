from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'upe_calendar.views.calendar', name='calendar'),
    url(r'^get_calendar_info/$', 'upe_calendar.views.get_calendar_info', name='get_calendar_info'),
)
