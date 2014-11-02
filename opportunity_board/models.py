from datetime import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date_published = models.DateTimeField(default=timezone.now(), blank=True)
	date_deadline = models.DateTimeField(default=timezone.now(), blank=True)

	def __str__(self):
		return self.content

	def was_published_recently(self):
		return self.date_published >= timezone.now() - datetime.timedelta(days=1)




