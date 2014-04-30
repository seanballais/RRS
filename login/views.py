from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
	return HttpResponse("<h1>Limher was here.</h1><p><i>-Limher</i></p>")