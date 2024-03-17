from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('This is a boy views which is created by harry')

def paths(request):
    return HttpResponse('This is a paths views which is created by harry')