from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'upe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'opportunity_board.views.index', name='opportunity_board_index'),
    url(r'^create/$', 'opportunity_board.views.create_post', name='create'),
    url(r'^delete/(?P<post_id>[0-9]+)/$', 'opportunity_board.views.delete_post', name='delete'),
    url(r'^post/(?P<post_id>[0-9]+)/$', 'opportunity_board.views.display_post', name='post'),
)