from django.shortcuts import render
from django.http import HttpResponse
from login.forms import LoginForm
from django.views.generic.edit import FormView

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Limher was here.</h1><p><i>-Limher</i></p>")

def LoginView(FormView):
	template_name = "template.html"
	form_class = LoginForm
	success_url = "" # Add User Panel URL here

	def form_valid(self, form):
		form.authenticate_form()
		return super(LoginView, self).form_valid(form)