from django.contrib import admin
from userpanel.models import Room, Equipment, ReserveInfo, UseInfo
from login.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserAdmin(admin.ModelAdmin):
""" This will display the forms that will need input """
    fieldsets = [
        ('Username',               {'fields': ['username']}),
        ('Password',               {'fields': ['password']}),
        ('E-mail Address',         {'fields': ['emailadd']}),
        ('User Priviliges',        {'fields': ['user_privileges']}),
        ('Name',                   {'fields': ['firstname', 'lastname']}),
    ]
    list_display = ('username', 'password', 'emailadd', 'user_privileges', 'firstname', 'lastname')

""" In this part of the admin, you should only enter the password in a pbkdf2 hash with sha-256 form """

admin.site.register(CustomUser, UserAdmin)