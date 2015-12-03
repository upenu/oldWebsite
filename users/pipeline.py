from .models import UserProfile

from requests import request, HTTPError

from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseRedirect


def save_profile(backend, user, response, *args, **kwargs):
    if kwargs['is_new']:
        attrs = {'user': user, 'approved': False, 'year_joined': 'F15'}
        attrs = dict(attrs.items())
        UserProfile.objects.create(**attrs)

def save_profile_picture(backend, user, response, details,
                         is_new=False,*args,**kwargs):
    url = ""
    if backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
    if backend.name == 'google-oauth2':
       if response.get('image') and response['image'].get('url'):
           url = response['image'].get('url')
           ext = url.split('.')[-1]
    if backend.name == 'twitter':
        url = response.get('profile_image_url', '').replace('_normal','')
    if is_new:
        try:
            response = request('GET', url, params={'type': 'large'})
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            up = UserProfile.objects.get(user=user)
            up.picture.save('{0}_social.jpg'.format(user.username),
                                   ContentFile(response.content))
            up.save()

def user_login(backend, user, response, details, is_new=False, *args, **kwargs):
    up = UserProfile.objects.get(user=user)
    if not up.approved:
            return HttpResponse("Your account has not been approved yet.")
