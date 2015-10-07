from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(max_length=10000, blank=True, null=True)
    location = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=100)
    banner = models.CharField(max_length=100)
    def __str__(self):
        return self.name
