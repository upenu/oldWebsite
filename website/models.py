from django.db import models
import datetime

class Post(models.Model):
	POST_TYPES = (
		(1, 'Instagram'),
		(2, 'Facebook'),
		(3, 'Twitter')
		)

	text = models.CharField(max_length=1001, default='default post text')
	url = models.CharField(max_length=250, default='https://twitter.com/berkeleyUPE')
	date = models.DateField()
	#img_video = models.ImageField(default='static/website/images/icons/twitter.png')
	img_video = models.ImageField(default='static/website/images/icons/post1.jpg')
	media = models.ImageField(default='static/website/images/icons/instagram_logo.png')
	likes = models.CharField(max_length=1001, default='420')
