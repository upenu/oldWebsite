from django.conf import settings
from django.contrib.auth.models import User, check_password
from website.models import *

class CustomBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = None
            user = User.objects.get(username=username)
            up = UserProfile.objects.get(user=user)
            if up.approved and user.check_password(password):
                print("Approved user " + username + " logged in.") 
                return user
            else:
                print("User " + username + " has not been approved. ")
                return 'unapproved' 
        except (UserProfile.DoesNotExist, User.DoesNotExist):
            print("============" + str(user))
            if user and user.is_staff:
            	return user
            print("User does not exist.")
            return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
