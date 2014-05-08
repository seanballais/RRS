from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from login.models import CustomUser
from userpanel.models import Room, Equipment, ReserveInfo
from django.contrib.auth.models import User
from userpanel.forms import ReserveInfoForm
from django.core.context_processors import csrf

# Create your views here.

def userpanel(request):
    if request.user.is_authenticated():
        user_list = User.objects.all()
        room_list = Room.objects.all()
        equipment_list = Equipment.objects.all()
        if request.method == 'POST':
            form = ReserveInfoForm(request.POST)
            if form.is_valid():
                form.save()
        else:
			form = ReserveInfoForm()
        return render_to_response('userpanel/userpanel.html', {'user_list': user_list, 'room_list': room_list, 'equipment_list': equipment_list, 'form': form,})

    else:
        return HttpResponseRedirect('/login/')