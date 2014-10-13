from django.db import models
from users.models import UserProfile

# Create your models here.
class Question(models.Model):
    question_text = models.TextField()
    answer_text = models.TextField()
    

    def __str__(self):
        return '%s %s' % (self.question_text, self.answer_text)

class PersonalQuestion(models.Model):
    stars = models.IntegerField()
    quest = models.ForeignKey('Question', blank=True, null=True)
    user = models.OneToOneField(UserProfile, blank=True, null=True)