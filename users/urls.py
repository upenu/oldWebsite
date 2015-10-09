from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

  url('', include('social.apps.django_app.urls', namespace='social')),
  url('', include('django.contrib.auth.urls', namespace='auth')),
)
