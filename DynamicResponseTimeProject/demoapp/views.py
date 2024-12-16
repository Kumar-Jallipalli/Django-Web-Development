from django.shortcuts import render

## from datetime module import datetime package
from datetime import datetime

from django.http import HttpResponse

# Create your views here.
def datetime_view(request):

    ## defining Greeting message using a variable
    msg = "<h1> Hello World, "

    ## Making a Dynamic Greeting messgage using datetime package
    date = datetime.now()
    hours = int(date.strftime("%H"))

    if (hours < 12):
        msg = msg + "Good Morning..!"
    elif (hours < 16):
        msg = msg + "Good Afternoon..!"
    elif (hours < 19):
        msg = msg + "Good Evening..!"
    else:
        msg = msg + "Good Night"

    msg = msg + "</h1> <hr>"
    msg += "<h2> Current date & time : " + str(date) + "</h2>"

    print(msg)
    
    return HttpResponse(msg)
