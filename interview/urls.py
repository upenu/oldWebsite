from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', 'interview.views.index', name='interview'),
#    url(r'^$', 'website.views.index', name='website-index'),


    # ex: /interview/
    url(r'^$', interview.views.index, name='index'),
    # ex: /interview/5/
    url(r'^(?P<question_id>\d+)/$', interview.views.detail, name='detail'),
    # ex: /interview/5/results/
    url(r'^(?P<question_id>\d+)/results/$', interview.views.results, name='results'), #interiew.views.results or views.results ??
)