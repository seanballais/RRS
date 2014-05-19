from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from login.models import CustomUser
from userpanel.models import Room, Equipment, ReserveInfo, UseInfo
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, logout
from userpanel.forms import ReserveInfoForm, UseInfoForm
from django.core.context_processors import csrf

# Create your views here.

def userpanel_rooms(request):
    if request.user.is_authenticated():
        #user_list = CustomUser.objects.all()
		all_reserved = []
		user_pending = []
		my_reserved = []
		room_list = Room.objects.all()
		reserveinfo_list = ReserveInfo.objects.all()
		useinfo_list = UseInfo.objects.all()
		user= request.user
		for room in room_list:
			for event in room.reserveinfo_set.all():
				if event.user == user and event.Status == 'Reserved' and room not in my_reserved:
					my_reserved.append(room)
				if event.Status == 'Reserved' and room not in all_reserved:
					all_reserved.append(room)
				if event.Status == 'Pending' and event.user == user and room not in user_pending:
					user_pending.append(room)
		return render_to_response('userpanel/userpanel.html', {'room_list': room_list, 'reserveinfo_list': reserveinfo_list, 'useinfo_list': useinfo_list, 'all_reserved' : all_reserved,  'my_reserved' : my_reserved, 'user_pending': user_pending, 'user': user,})
    else:
        return HttpResponseRedirect('/login/')
		
def userpanel_equip(request):
	if request.user.is_authenticated():
		all_reserved = []
		user_pending = []
		my_reserved = []
		equipment_list = Equipment.objects.all()
		reserveinfo_list = ReserveInfo.objects.all()
		useinfo_list = UseInfo.objects.all()
		user= request.user
		for equipment in equipment_list:
			for use in equipment.useinfo_set.all():
				if use.user == user and use.Status == 'Reserved' and equipment not in my_reserved:
					my_reserved.append(equipment)
				if use.Status == 'Reserved' and equipment not in all_reserved:
					all_reserved.append(equipment)
				if use.Status == 'Pending' and use.user == user and equipment not in user_pending:
					user_pending.append(equipment)
		return render_to_response('userpanel/userpanel_equip.html', {'equipment_list': equipment_list, 'reserveinfo_list': reserveinfo_list,  'useinfo_list': useinfo_list,  'all_reserved' : all_reserved, 'my_reserved' : my_reserved, 'user_pending': user_pending, 'user' : user,})
	else:
		return HttpResponseRedirect('/login/')	
		

def room(request, room_id):
    r = get_object_or_404(Room, pk=room_id)
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        #form = ReserveInfoForm(request.POST)
        #if form.is_valid():
            '''room=request.POST.get('room')
            Eventname=request.POST.get('name')
            EventDescription=request.POST.get('description')
            StartDate=request.POST.get('startdate')
            EndDate=request.POST.get('enddate')
            StartTime=request.POST.get('starttime')
            EndTime=request.POST.get('endtime')
            Status=request.POST.get('status')'''
            #user = get_user_model()
            if(request.user.user_privileges == 1 or request.user.user_privileges == 2):
                r.reserveinfo_set.create(   user=request.user, 
                                            Eventname=request.POST.get('name'), 
                                            EventDescription=request.POST.get('description'), 
                                            StartDate=request.POST.get('startdate'), 
                                            EndDate=request.POST.get('enddate'), 
                                            StartTime=request.POST.get('starttime'), 
                                            EndTime=request.POST.get('endtime'), 
                                            Status="Reserved")
            else:
                r.reserveinfo_set.create(   user=request.user, 
                                            Eventname=request.POST.get('name'), 
                                            EventDescription=request.POST.get('description'), 
                                            StartDate=request.POST.get('startdate'), 
                                            EndDate=request.POST.get('enddate'), 
                                            StartTime=request.POST.get('starttime'), 
                                            EndTime=request.POST.get('endtime'), 
                                            Status="Pending")
            r.save()
            #form.save()
            return HttpResponseRedirect('/userpanel/rooms/')
    else:
        form = ReserveInfoForm()

    return render_to_response('userpanel/room.html', {'form': form, 'room':r,}, csrfContext)

def equipment(request, equipment_id):
    e = get_object_or_404(Equipment, pk=equipment_id)
    csrfContext = RequestContext(request)
    if request.method == 'POST':
            if(request.user.user_privileges == 1 or request.user.user_privileges == 2):
                e.useinfo_set.create(   user=request.user, 
                                        Eventname=request.POST.get('name'), 
                                        EventDescription=request.POST.get('description'), 
                                        StartDate=request.POST.get('startdate'), 
                                        EndDate=request.POST.get('enddate'), 
                                        StartTime=request.POST.get('starttime'), 
                                        EndTime=request.POST.get('endtime'), 
                                        Status="Reserved")
            else:
                e.useinfo_set.create(   user=request.user, 
                                        Eventname=request.POST.get('name'), 
                                        EventDescription=request.POST.get('description'), 
                                        StartDate=request.POST.get('startdate'), 
                                        EndDate=request.POST.get('enddate'), 
                                        StartTime=request.POST.get('starttime'), 
                                        EndTime=request.POST.get('endtime'), 
                                        Status="Pending")
            e.save()
            #form.save()
            return HttpResponseRedirect('/userpanel/equipments')
    else:
        form = UseInfoForm()

    return render_to_response('userpanel/equipment.html', {'form': form, 'equipment':e,}, csrfContext)

def event(request, reserveinfo_id):
    e = get_object_or_404(ReserveInfo, pk=reserveinfo_id)
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        if(request.user.user_privileges == 1 or request.user.user_privileges == 2):
            e.Status="Reserved"
        e.save()
        #form.save()
        return HttpResponseRedirect('/userpanel/')
    else:
        form = ReserveInfoForm()

    return render_to_response('userpanel/event.html', {'form': form, 'event':e,}, csrfContext)

def use(request, useinfo_id):
    e = get_object_or_404(UseInfo, pk=useinfo_id)
    csrfContext = RequestContext(request)
    if request.method == 'POST':
        if(request.user.user_privileges == 1 or request.user.user_privileges == 2):
            e.Status="Reserved"
        e.save()
        #form.save()
        return HttpResponseRedirect('/userpanel/')
    else:
        form = ReserveInfoForm()

    return render_to_response('userpanel/use.html', {'form': form, 'use':e,}, csrfContext)

def reserve(request, room_id):
    r = get_object_or_404(Room, pk=room_id)
    try:
        selected_choice = r.reserveinfo_set.create( room=request.POST.get('room'), 
                                                    Eventname=request.POST.get('name'), 
                                                    EventDescription=request.POST.get('description'), 
                                                    StartDate=request.POST.get('startdate'), 
                                                    EndDate=request.POST.get('enddate'), 
                                                    StartTime=request.POST.get('starttime'), 
                                                    EndTime=request.POST.get('endtime'), 
                                                    Status=request.POST.get('status'))
    except (KeyError, ReserveInfo.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('/userpanel/{{ room.pk }}/', {
            'room': r,
            'error_message': "All field are not filled correctly",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('/userpanel/'))

def logout_view(request):
    logout(request)
    
    return HttpResponseRedirect('/login/')