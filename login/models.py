from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User, PermissionsMixin

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, emailadd, user_privileges):
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
        	username = username,
            emailadd = CustomUserManager.normalize_email(emailadd),
            user_privileges = user_privileges,
            is_staff = True,
            is_admin = True,
            is_superuser = False
        )
 
        user.set_password(password)
        user.save(using = self._db)
        return user
 
    def create_superuser(self, username, password, emailadd):
        user = self.create_user(username, password = password, emailadd = emailadd, user_privileges = 1)

        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
	objects 						  = CustomUserManager()
	id 								  = models.AutoField(primary_key = True)
	username			              = models.CharField('Username', max_length = 256, unique = True)
	emailadd			              = models.EmailField('Email Address', max_length = 256)
	UserPrivilegesChoices             = ((1, 'Superadmin'),(2, 'Admin'),(3, 'Faculty'),(4, 'Student'))
	user_privileges		              = models.IntegerField('User Privileges', choices = UserPrivilegesChoices)
	firstname 			              = models.CharField('First Name', max_length = 256)
	lastname			              = models.CharField('Last Name', max_length = 256)

	is_active 						  = models.BooleanField('Active?', default = True)
	is_admin 					 	  = models.BooleanField('Administrator?', default = False)
	is_staff                          = models.BooleanField('Staff?', default = True)
	
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['emailadd']

	def user_privileges_type(self):
		return self.user_privileges

	@property
	def is_staff(self):
		return self.is_admin

	def has_perm(self, perm, obj=None):
		return True
	
	def has_module_perms(self, app_label):
		return True

	def __unicode__(self):
		return self.username

	def get_full_name(self):
		# For this case we return email. Could also be User.first_name User.last_name if you have these fields
		return self.firstname + self.lastname + self.emailadd

	def get_short_name(self):
		return self.emailadd