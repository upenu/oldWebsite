from .models import UserProfile

from requests import request, HTTPError

from django.core.files.base import ContentFile

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook' and kwargs['is_new']:
        attrs = {'user': user, 'approved': False, 'year_joined': 'F15'}
        attrs = dict(attrs.items())
        UserProfile.objects.create(**attrs)

def save_profile_picture(backend, user, response, details,
                         is_new=False,*args,**kwargs):

    if is_new and backend.name == 'facebook':
        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

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

def user_login(backend, user, response, details, is_new=FALSE, *args, **kwargs):
    up = UserProfile.objects.get(user=user)
    if up.approved == False:
            return HttpResponse("Your account has not been approved yet.")
