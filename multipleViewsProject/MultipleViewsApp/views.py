from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hydjobs_view(request):
    res = "<h1>Jobs related to Hyderabad Location can be found here..</h1>"
    return HttpResponse(res)

def bangjobs_view(request):
    res = "<h1>Jobs related to Bangalore Location can be found here..</h1>"
    return HttpResponse(res)

def punejobs_view(request):
    res = "<h1>Jobs related to Pune Location can be found here..</h1>"
    return HttpResponse(res)

def delhijobs_view(request):
    res = "<h1>Jobs related to Delhi Location can be found here..</h1>"
    return HttpResponse(res)