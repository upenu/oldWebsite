from django import forms
from django.contrib.auth.models import User
from website.models import *

class CompletionForm(forms.Form):
    requirements = forms.ModelChoiceField(queryset=Requirement.objects.all()) 
    candidates = forms.ModelChoiceField(queryset=CandidateProfile.objects.all())

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_type',) 

class ResumeUploadForm(forms.Form):
    resume = forms.FileField(label='Upload a PDF')

class ProfilePicChangeForm(forms.Form):
    picture = forms.ImageField(label='')

