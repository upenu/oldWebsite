from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', 'interview.views.index', name='interview'),
#    url(r'^$', 'website.views.index', name='website-index'),
)