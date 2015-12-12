from django.db import models
from django_markdown.models import MarkdownField

class QuestionTag(models.Model):
    tag = models.CharField(max_length=100)
    def __str__(self):
        return self.tag

class Question(models.Model):
    tags = models.ManyToManyField(QuestionTag)
    title = models.CharField(max_length=100)
    text = MarkdownField()
    solution = MarkdownField()
    difficulty = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.title
    

class QuestionImage(models.Model):
    question = models.ForeignKey(Question)
    img = models.ImageField(upload_to='question_images', null=True)
    for_soln = models.BooleanField(default=False) # whether this image is for the soln of the question
    







