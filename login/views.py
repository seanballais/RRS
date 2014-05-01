from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Limher was here.</h1><p><i>-Limher</i></p><h2>Need help! Login might be pushed to Sprint 2!</h2>")
