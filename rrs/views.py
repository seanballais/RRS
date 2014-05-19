from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from userpanel.models import Room

def about(request):
	room_list = Room.objects.all()
	return render_to_response('about.html', {'room_list': room_list, })
	
def aboutus(request):
	context=''
	return render(request, 'aboutus.html', context)