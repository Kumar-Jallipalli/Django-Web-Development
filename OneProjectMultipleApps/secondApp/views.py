from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_view2(request):
    res = "<h1>This Request/Message is from SECOND APP</h1>"
    return HttpResponse(res)
