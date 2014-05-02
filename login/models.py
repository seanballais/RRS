from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user 				= models.OneToOneField(User)
	userID 				= models.AutoField(primary_key = True)
	username			= models.CharField(max_length = 256, unique = True)
	password			= models.CharField(max_length = 256)
	emailadd			= models.CharField(max_length = 256)
	user_privileges		= models.TextField()
	firstname 			= models.TextField()
	lastname			= models.TextField()
	middlename			= models.TextField()
	def __unicode__(self):
		return self.username