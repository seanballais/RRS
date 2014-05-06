from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user 				              = models.OneToOneField(User)
	userID 				              = models.AutoField(primary_key = True)
	username			              = models.CharField(max_length = 256, unique = True)
	password			              = models.CharField(max_length = 256)
	emailadd			              = models.CharField(max_length = 256)
	user_privileges		              = models.TextField()
	firstname 			              = models.TextField()
	lastname			              = models.TextField()
	middlename			              = models.TextField()
	def __unicode__(self):
		return self.username
class ReserveInfo(models.Model):
	EventID							= models.AutoField(primary_key = True)
	Eventname						= models.CharField(max_length = 256, unique = True)
	EventDescription				= models.TextField('Event Description     (Optional)', blank=True)
	StartDate						= models.DateField('Start Date')
 	StartTime						= models.TimeField('Start Time')
 	EndDate							= models.DateField('End Date')
 	EndTime							= models.TimeField('End Time')
 	StatusChoices                = ((1, 'Available'),(2, 'Pending'),(3, 'Reserved'))


 	Status							= models.IntegerField('Status',choices=StatusChoices)
