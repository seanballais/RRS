from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from login.models import UserProfile
from userpanel.models import Room, Equipment, ReserveInfo
from django.contrib.auth.models import User

# Create your views here.

class UserView(generic.ListView):
	# For the next sprint, add a function to check if a user is logged in. If not login, redirect user to login
    context_object_name = 'home_list'    
    template_name = 'userpanel/users.html'
    queryset =  ''

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['room_list'] = Room.objects.all()
        context['equipment_list'] = Equipment.objects.all()
        return context