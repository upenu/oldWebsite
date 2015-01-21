from django import forms
from django.contrib.auth.models import User
from users.models import *

# class CompletionForm(forms.Form):
#     requirements = forms.ModelChoiceField(queryset=Requirement.objects.all()) 
#     candidates = forms.ModelChoiceField(queryset=CandidateProfile.objects.all())

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

class EarlyApplicantForm(forms.ModelForm):
    CLASS_CHOICES = (
        ('CS 61A/AS', 'CS 61A/AS'),
        ('CS 61B/L', 'CS 61B/L'),
        ('CS 61C', 'CS 61C'),
        ('CS 70',   'CS 70'),  
        ('Math 1A', 'Math 1A'),
        ('Math 1B', 'Math 1B'),
        ('Math 54', 'Math 54'),
    )
    courses_taking = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CLASS_CHOICES)
    courses_taken = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CLASS_CHOICES)
    courses_a_minus = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=CLASS_CHOICES)

    class Meta:
        model = EarlyApplicant
        fields = ('reported_gpa', 'courses_taking', 'courses_taken', 'courses_a_minus', 
            'uploaded_transcript', 'motivation_upe')

class ResumeUploadForm(forms.Form):
    resume = forms.FileField(label='Upload a PDF')

class ProfilePicChangeForm(forms.Form):
    picture = forms.ImageField(label='')
        
