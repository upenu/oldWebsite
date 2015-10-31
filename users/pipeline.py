from .models import UserProfile

from requests import request, HTTPError

from django.core.files.base import ContentFile

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook' and kwargs['is_new']:
        attrs = {'user': user}
        attrs = dict(attrs.items())
        UserProfile.objects.create(**attrs)
