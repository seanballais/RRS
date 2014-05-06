from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user 				              = models.OneToOneField(User)
	userID 				              = models.AutoField(primary_key = True)
	username			              = models.CharField(max_length = 256, unique = True)
	password			              = models.CharField(max_length = 256)
	emailadd			              = models.CharField(max_length = 256)
	UserPrivilegesChoices             =((1, 'Superadmin'),(2,'Admin'),(3,'Faculty'),(4,'Student'))
	user_privileges		              = models.IntegerField('User Privileges',choices=UserPrivilegesChoices)

	firstname 			              = models.CharField(max_length = 256)
	lastname			              = models.CharField(max_length = 256)
	middlename			              = models.CharField(max_length = 256)
	def __unicode__(self):
		return self.username
