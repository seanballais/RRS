from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
<<<<<<< HEAD
	user 				= models.OneToOneField(User)
	userID 				= models.AutoField(primary_key = True)
	username			= models.CharField(max_length = 256, unique = True)
	password			= models.CharField(max_length = 256)
	emailadd			= models.CharField(max_length = 256)
	user_privileges		= models.TextField()
	firstname 			= models.TextField()
	lastname			= models.TextField()
	middlename			= models.TextField()
=======
	userID 			= models.AutoField(primary_key = True)
	username		= models.CharField(max_length = 256, unique = True)
	password		= models.CharField(max_length = 256)
	emailadd		= models.CharField(max_length = 256)
	user_privileges	= models.TextField()
	firstname 		= models.TextField()
	lastname		= models.TextField()
	middlename		= models.TextField()
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.username

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
>>>>>>> 1a00bc241e1087cf3a15266eb5765240f10e1d0b
