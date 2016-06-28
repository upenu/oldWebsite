from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('website.urls')),
    url(r'^calendar/', include('upe_calendar.urls')),

    url(r'^officers/$', 'users.views.officers', name='officers'),
    url(r'^members/$', 'users.views.members', name='members'),
    url(r'^members/filter/$', 'users.views.members_filter', name='members_filter'),
    url(r'^interest/$', 'users.views.interest', name='interest'),
    url(r'^alumni/$', 'users.views.alumni', name='alumni'),
    url(r'^officehours/$', 'users.views.officehours', name='officehours'),
    url(r'^currentofficers/$', 'users.views.currentofficers', name='currentofficers'),
    url(r'^requirements/$', 'users.views.requirements', name='requirements'),
    url(r'^register/$', 'users.views.register', name='register'),
    url(r'^myprofile/$', 'users.views.myprofile', name='myprofile'),
    url(r'^login/$', 'users.views.user_login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^accounts/password_reset', 'django.contrib.auth.views.password_reset', {'template_name': 'users/password_reset_form.html'}),
    url(r'^accounts/', include('django.contrib.auth.urls')),

    url(r'^approval_dashboard/$', 'users.views.officer_approval_dashboard', name='officer_approval_dashboard'),
    url(r'approve_user/(?P<user_id>[0-9]+)/$', 'users.views.approve_user', name='approve_user'),
    url(r'reject_user/(?P<user_id>[0-9]+)/$', 'users.views.reject_user', name='reject_user'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT,
    }),

)
