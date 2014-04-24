from django import forms
from django.contrib.auth.models import User
from website.models import *

class CompletionForm(forms.Form):
    pass
    #requirements = forms.ModelChoiceField(queryset= models.Requirement.objects.all()) 
    #candidates = forms.ModelChoiceField(queryset = models.CandidateProfile.objects.all())

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('approved', 'type') 
