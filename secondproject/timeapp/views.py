from django.shortcuts import render

## Importing datetime module
import datetime

## importing HttpResonse Object
from django.http import HttpResponse

# Create your views here.
def time_info(request):
    print('Hello')  ## This will print in the Server's Console but Not displayed to End User
    time = datetime.datetime.now()
    res = '<h1> Current Date & Time : ' + str(time) + '</h1>'
    return HttpResponse(res)