from django.shortcuts import render

# Importing the HttpResponse Class from django's http module
from django.http import HttpResponse

# Create your views here.
def display(request):
    res = "This is my First Response in Django Web Developemnt"
    # Returning the response as a HttpResponse Object [ as Browser cannot understand String ]
    return HttpResponse(res)

"""
    - This above function will be called by WebServer by passing  HttpRequest Object as the function argument
    - WebServer always provides the HttpRequest Object as an function argument, which can be accessed using "request"
"""