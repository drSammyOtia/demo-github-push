from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def demo(request):
    return HttpResponse('This is github push demo')
