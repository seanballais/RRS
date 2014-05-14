from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, get_user_model, logout

def user_login(request):
    """ User Login System Backend """
    user = get_user_model()
    state = ""
    username = password = ''
    csrfContext = RequestContext(request)
    if request.user.is_authenticated(): # Redirect back to the userpanel if the user is already logged in
        return HttpResponseRedirect('/userpanel/')
    else:
        if request.POST: # Authenticate if it is an anonymous user
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect("/userpanel")
                else:
                    state = "Your account is not active, please contact the site admin."
            else:
                state = "Your username and/or password were incorrect."
        return render_to_response('login/login.html',{'state': state, 'username': username}, csrfContext) # Extend this code sentence
def logout_view(request):
    logout(request)
    return redirect('/login/')