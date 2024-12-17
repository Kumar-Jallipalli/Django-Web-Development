from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse('<h1> FIRST View </h1>')

def second_view(request):
    return HttpResponse('<h1> SECOND View </h1>')

def third_view(request):
    return HttpResponse('<h1> THIRD View </h1>') 

def fourt_view(request):
    return HttpResponse('<h1> FOURTH View </h1>') 

def fifth_view(request):
    return HttpResponse('<h1> FIFTH View </h1>')
