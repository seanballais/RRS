from django.http import HttpResponse
<<<<<<< HEAD
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login


def user_login(request):
    state = "Please login..."
    username = password = ''
    csrfContext = RequestContext(request)
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('login.html',{'state': state, 'username': username}, csrfContext) # Extend this code sentence
=======
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
>>>>>>> 1a00bc241e1087cf3a15266eb5765240f10e1d0b
