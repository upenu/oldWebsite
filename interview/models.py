from django.db import models

# Create your models here.
class Question(models.Model):
	question_text = models.TextField()
	answer_text = models.TextField()

	def __str__(self):
		return '%s %s' % (self.question_text, self.answer_text)