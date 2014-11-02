from django import forms
from opportunity_board.models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content')
