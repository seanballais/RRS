from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, emailadd, user_privileges):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
        	username = username,
            emailadd = CustomUserManager.normalize_email(emailadd),
            user_privileges = user_privileges
        )
 
        user.set_password(password)
        user.save(using = self._db)
        return user
 
    def create_superuser(self, username, password, emailadd):
        user = self.create_user(username, password = password, emailadd = emailadd, user_privileges = 1)

        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
	objects 						  = CustomUserManager()
	id 								  = models.AutoField(primary_key = True)
	username			              = models.CharField('Username', max_length = 256, unique = True)
	emailadd			              = models.EmailField('Email Address', max_length = 256)
	UserPrivilegesChoices             = ((1, 'Superadmin'),(2, 'Admin'),(3, 'Faculty'),(4, 'Student'))
	user_privileges		              = models.IntegerField('User Privileges', choices = UserPrivilegesChoices)
	firstname 			              = models.CharField('First Name', max_length = 256)
	lastname			              = models.CharField('Last Name', max_length = 256)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['emailadd']

	def user_privileges_type(self):
		return self.user_privileges

	def __unicode__(self):
		return self.username