from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request,"basic/index.html")

def aman(request):
	return HttpResponse("Server Runing OK!")

def	server(request):
	return HttpResponse("Server Ok!")
def	greet(request, name):
	return render(request,"basic/greet.html",{
		"name": name.capitalize()
	})
