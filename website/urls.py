from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^oh/$', 'website.views.oh', name='oh'),
    url(r'^ir/$', 'website.views.ir', name= 'ir'),
    url(r'^bookinterview/(?P<slot_id>[a-z]+[0-9]+)/$', 'website.views.book_interview', name='book_interview'),
    url(r'^interview/$', 'website.views.interview', name='interview'),
    url(r'^confirminterview/$', 'website.views.confirm_interview', name='confirm_interview'),
    url(r'^requirements/$', 'website.views.requirements', name='verify_requirements'),
)
