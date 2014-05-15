from django.contrib import admin
from userpanel.models import Room, Equipment, ReserveInfo, UseInfo
from login.models import CustomUser

# Register your models here.

class ReserveInline(admin.TabularInline):
    model = ReserveInfo
    extra = 3
    
class RoomAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                   {'fields': ['name']}),
        ('Number',                 {'fields': ['number']}),
        ('Capacity',               {'fields': ['capacity']}),
    ]
    inlines = [ReserveInline]
    list_display = ('name', 'number', 'capacity')

class UseInline(admin.TabularInline):
    model = UseInfo
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                   {'fields': ['name']}),
        ('Description',            {'fields': ['description']}),
        #('Picture',               {'fields': ['picture']}),
    ]
    inlines = [UseInline]
    list_display = ('name', 'description')

'''class ReserveInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Name',                         {'fields': ['Eventname']}),
        ('Event Description(Optional)',        {'fields': ['EventDescription']}),
        ('Start Date',                         {'fields': ['StartDate']}),
        ('Start Time',                         {'fields': ['StartTime']}),
        ('End Date',                           {'fields': ['EndDate']}),
        ('End Time',                           {'fields': ['EndTime']}),
        ('Status',                             {'fields': ['Status']}), 
        ('User',                               {'fields': ['user']}), 
    ]
    list_display = ('Eventname','EventDescription', 'StartDate', 'StartTime', 'EndDate', 'EndTime', 'Status', 'user')'''
    
admin.site.register(Room, RoomAdmin)
admin.site.register(Equipment, EquipmentAdmin)





