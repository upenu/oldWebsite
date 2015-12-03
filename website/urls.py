from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'website.views.index', name='index'),
    url(r'^oh/$', 'website.views.oh', name='oh'),

    #url('', include('social.apps.django_app.urls', namespace='social')),
    #url('', include('django.contrib.auth.urls', namespace='auth')),
)
