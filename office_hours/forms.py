from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from users.models import *
from office_hours.models import *

class InterviewReservationForm(ModelForm):
    class Meta:
        model = InterviewReservation
        fields = ['interviewee_email', 'available']

#class InterviewForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(forms.ModelForm, self).__init__(*args, **kwargs)
    #     self.fields['email'].help_text = None
    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'username', 'email', 'password')
#    class Meta:
#        model = InterviewReservation
#        fields = ('interviewee_email','available')


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
