from django import forms
from django.contrib.auth.models import User
from users.models import *

class CompletionForm(forms.Form):
    requirement = forms.ModelChoiceField(label="requirement", queryset=Requirement.objects.all()) 
    candidates = forms.ModelMultipleChoiceField(label="candidates", queryset=CandidateProfile.objects.order_by('name'))
    note = forms.CharField(label="note", max_length=140)

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.Textarea)

class RequirementForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    description = forms.CharField(label='description', max_length=500)
    num_required = forms.IntegerField(label='num_required')

class editReqForm(forms.Form):
    requirement = forms.ModelChoiceField(label="requirement", queryset=Requirement.objects.all()) 
    delete= forms.BooleanField(label='delete')
    num_required = forms.IntegerField(label='num_required', initial=0)

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
        
