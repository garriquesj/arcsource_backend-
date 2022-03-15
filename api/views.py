from django.shortcuts import render, HttpResponse

# Create your views here.
def Index(render):
    return HttpResponse('this works')