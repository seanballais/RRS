from django.contrib import admin
from userpanel.models import Room, Equipment, ReserveInfo
from login.models import UserProfile

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('UserID',                 {'fields': ['userID']}),
        ('Username',               {'fields': ['username']}),
        ('Password',               {'fields': ['password']}),
        ('E-mail Address',         {'fields': ['emailadd']}),
        ('User Priviliges',        {'fields': ['user_privileges']}),
        ('Name',                   {'fields': ['firstname', 'middlename', 'lastname'], 'classes': ['collapse']}),
    ]
    list_display = ('username', 'password', 'emailadd', 'user_privileges', 'firstname', 'middlename', 'lastname')

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                   {'fields': ['name']}),
        ('Number',                 {'fields': ['number']}),
        ('Capacity',               {'fields': ['capacity']}),
    ]
    list_display = ('name', 'number', 'capacity')

class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                   {'fields': ['name']}),
        ('Description',            {'fields': ['description']}),
        #('Picture',               {'fields': ['picture']}),
    ]
    list_display = ('name', 'description')
class ReserveInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Name',                         {'fields': ['Eventname']}),
        ('Event Description(Optional)',        {'fields': ['EventDescription']}),
        ('Start Date',                         {'fields': ['StartDate']}),
        ('Start Time',                         {'fields': ['StartTime']}),
        ('End Date',                           {'fields': ['EndDate']}),
        ('End Time',                           {'fields': ['EndTime']}),
        ('Status',                             {'fields': ['Status']}), 
    ]
    list_display = ('Eventname','EventDescription', 'StartDate', 'StartTime', 'EndDate', 'EndTime', 'Status')
class  UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username',                           {'fields': ['username']}),
        ('Password',                           {'fields': ['password']}),
        ('Email Address',                      {'fields': ['emailadd']}),
        ('User Priviliges',                    {'fields': ['user_privileges']}),
        ('First Name',                         {'fields': ['firstname']}),
        ('Middle Name',                        {'fields': ['middlename']}),
        ('last Name',                          {'fields': ['lastname']}),
    ]
    list_display = ('username', 'user_privileges', 'firstname', 'middlename', 'lastname' )
    







#Uncomment this part if forst time deploy then recomment this again
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(ReserveInfo, ReserveInfoAdmin)




