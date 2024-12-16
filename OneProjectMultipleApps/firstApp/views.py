from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view1(request):
    res = "<h1>This Request/Message is from FIRST APP</h1>"
    return HttpResponse(res)
