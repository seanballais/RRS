from django.shortcuts import render
from django.http import HttpResponse
from login.models import UserProfile, Room, Equipment

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Limher was here.</h1><p><i>-Limher</i></p>")

def UserPanel(request):
    latest_user_list = UserProfile.objects.order_by('username')
    latest_room_list = Room.objects.order_by('name')
    latest_equipment_list = Equipment.objects.order_by('name')
    items = [u.username for u in latest_user_list]
    items.append("\n")
    for r in latest_room_list:
    	items.append(r.name)
    items.append("\n")
    for e in latest_equipment_list:
    	items.append(e.name)
    output = ', '.join(i for i in items)
    return HttpResponse(output)