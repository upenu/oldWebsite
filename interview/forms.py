from django import forms
from interview.models import *

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question_text', 'answer_text', 'category', 'difficulty')
