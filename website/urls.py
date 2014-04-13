from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^officehours/$', 'website.views.officehours', name='officehours'),
    url(r'^currentofficers/$', 'website.views.currentofficers', name='currentofficers'),
    url(r'^requirements/$', 'website.views.requirements', name='requirements'),
)
