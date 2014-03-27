from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user = models.OneToOneField(User)
    family = models.CharField(max_length=200)
    committee = models.CharField(max_length=200)

    def get_progress(self):
        pass
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name



