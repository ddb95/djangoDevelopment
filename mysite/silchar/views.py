from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello Silcharians, welcome to django')

def homepageSilchar(request):
    return HttpResponse('This is the homepage of silcharians')