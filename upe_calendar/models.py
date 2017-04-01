from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_timestamp = models.BigIntegerField()
    description = models.TextField(max_length=10000, blank=True, null=True)
    location = models.CharField(max_length=100)
    banner = models.CharField(max_length=4096)
    facebookid = models.BigIntegerField(default=0)
    def __str__(self):
        return self.name
