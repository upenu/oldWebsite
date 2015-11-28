from django.db import models

class QuestionCategory(models.Model):
	category_title = models.CharField(max_length=100)

class Question(models.Model):
	question_category = models.ForeignKey(QuestionCategory)
	question_title = models.CharField(max_length=100)
	question_text = models.CharField(max_length=1000)
	question_soln = models.CharField(max_length=1000)
	question_difficulty = models.PositiveSmallIntegerField()

class QuestionImage(models.Model):
	question = models.ForeignKey(Question)
	img = models.ImageField(upload_to='question_images', null=True)
	for_soln = models.BooleanField(default=False) # whether this image is for the soln of the question







