from django.shortcuts import render
from django.views.generic import TemplateView


#from django.http import HttpResponse 
#for testing to see if works
# def TestView(request, **kwargs):
# 	return HttpResponse("yoyo")

# Create your views here.

class SplashView(TemplateView):
	template_name = 'index.html'
