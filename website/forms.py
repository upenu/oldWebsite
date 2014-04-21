from django import forms
from website import models

class CompletionForm(forms.Form):
    requirements = forms.ModelChoiceField(queryset= models.Requirement.objects.all()) 
    candidates = forms.ModelChoiceField(queryset = models.CandidateProfile.objects.all())
