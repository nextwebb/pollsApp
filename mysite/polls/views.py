from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Awesome job guys!  This is the index page, of our polls application')
