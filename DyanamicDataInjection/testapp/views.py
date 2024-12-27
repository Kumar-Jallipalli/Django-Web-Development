from django.shortcuts import render
from datetime import datetime
import random

# Create your views here.
def home_page (request) :
    names_list = [
        'Brad',
        'George',
        'Tom',
        'Shanks',
        'Zoro'
    ]
    msg_list = [
        'You will definitely get a JOB soon',
        'You will achieve your DREAMS',
        'You will WIN the RACE',
        'You will have no REGRETS',
        'You will RETIRE HAPPILY'
    ]
    time = datetime.now()

    name = random.choice(names_list)
    msg = random.choice(msg_list)

    my_dict = {
        'name' : name,
        'msg' : msg,
        'time' : time
    }
    return render(request, 'testapp/index.html', my_dict)
