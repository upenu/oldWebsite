from django.conf.urls import patterns, url
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^$', 'interview.views.index', name='interview'),
    url(r'^create/$', 'interview.views.create', name='create'),
    url(r'^allfavorites/$', 'interview.views.allfavorites', name='allfavorites'),
    url(r'^delete/(?P<question_id>[0-9]+)/$', 'interview.views.delete', name='delete'),
    url(r'^favorite/(?P<question_id>[0-9]+)/$', 'interview.views.favorite', name='favorite'),
    url(r'^rate/(?P<question_id>[0-9]+)/(?P<score>[0-9])/$', 'interview.views.rate', name='rate'),
    url(r'^question/(?P<question_id>[0-9]+)/$', 'interview.views.view_question', name='question'),
#    url(r'^$', 'website.views.index', name='website-index'),


#    # ex: /interview/
#    url(r'^$', interview.views.index, name='index'),
#    # ex: /interview/5/
#    url(r'^(?P<question_id>\d+)/$', interview.views.detail, name='detail'),
#    # ex: /interview/5/results/
#    url(r'^(?P<question_id>\d+)/results/$', interview.views.results, name='results'), #interiew.views.results or views.results ??
)
