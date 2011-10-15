from django.db import models

#imports from custom apps
from django.contrib.auth.models import User

class bookmarks(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length = 100)
	url = models.URLField()
	
	def __unicode__(self):
		return self.url