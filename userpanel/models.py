from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
	name		= models.CharField(max_length = 256)
	number		= models.IntegerField(default = 0)
	capacity	= models.IntegerField(default = 0)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

class Equipment(models.Model):
	name		= models.CharField(max_length = 256)
	description	= models.CharField(max_length = 256)
	#picture
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name