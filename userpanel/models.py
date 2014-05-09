from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
	name							= models.CharField(max_length = 256)
	number							= models.IntegerField(default = 0)
	capacity						= models.IntegerField(default = 0)
	room_id							= models.AutoField(primary_key = True)
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

class Equipment(models.Model):
	name							= models.CharField(max_length = 256)
	description						= models.CharField(max_length = 256)
	#equipment_id					= models.AutoField(primary_key = True)
	#picture
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

class ReserveInfo(models.Model):
	room                            = models.ForeignKey(Room)
	EventID							= models.AutoField(primary_key = True)
	Eventname						= models.CharField(max_length = 256, unique = True)
	EventDescription				= models.TextField('Event Description     (Optional)', blank=True)
	StartDate						= models.DateField('Start Date')
 	StartTime						= models.TimeField('Start Time')
 	EndDate							= models.DateField('End Date')
 	EndTime							= models.TimeField('End Time')
 	StatusChoices                   = ((1, 'Available'),(2, 'Pending'),(3, 'Reserved'))
 	Status							= models.IntegerField('Status',choices=StatusChoices)
 	
 	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Eventname

class UseInfo(models.Model):
	equipment                       = models.ForeignKey(Equipment)
	EventID							= models.AutoField(primary_key = True)
	Eventname						= models.CharField(max_length = 256, unique = True)
	EventDescription				= models.TextField('Event Description     (Optional)', blank=True)
	StartDate						= models.DateField('Start Date')
 	StartTime						= models.TimeField('Start Time')
 	EndDate							= models.DateField('End Date')
 	EndTime							= models.TimeField('End Time')
 	StatusChoices                   = ((1, 'Available'),(2, 'Pending'),(3, 'Reserved'))
 	Status							= models.IntegerField('Status',choices=StatusChoices)
 	
 	def __unicode__(self):  # Python 3: def __str__(self):
		return self.Eventname