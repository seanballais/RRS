from django.contrib import admin
from login.models import UserProfile, Room, Equipment

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
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

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)

# Register your models here.
