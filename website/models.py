from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    user = models.OneToOneField(User)
    #family = models.ForeignKey(Family)
    #committee = models.ForeignKey(Committee)

    def get_progress(self):
        pass
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Requirement(models.Model):
    candidates = models.ManyToManyField(Candidate)
    req_name = models.CharField(max_length=500)

    def __str__(self):
        return self.req_name

class Family(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Committee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

