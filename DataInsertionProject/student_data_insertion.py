import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataInsertionProject.settings')

import django
django.setup()

'''
These above lines are commonly used in a Django script 
to set up the environment for interacting with Django models and other components. 
Here's what each line does:

    1. import os: 
        This imports the os module, which allows you to interact with the operating system and environment variables.

    2. os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DataInsertionProject.settings'): 
        This sets the environment variable DJANGO_SETTINGS_MODULE to 'DataInsertionProject.settings'.
        DJANGO_SETTINGS_MODULE tells Django which settings file to use.
        If this variable is not already set, it defaults to 'DataInsertionProject.settings', 
        where DataInsertionProject is the name of your Django project.

    3. import django: 
        This imports the Django module, which contains all the functionalities of the Django framework.

    4. django.setup(): 
        This sets up the Django application. 
        It loads the settings specified by DJANGO_SETTINGS_MODULE and initializes the Django application.
        initializing Django --> loading the settings and setting up various components like the database connections. 

        This step is necessary if you're running a standalone script 
        that needs to interact with Django's models or other functionalities outside of the standard Django request/response cycle 
        (like in a management command or a custom script).

In summary, these lines prepare your script to use Django's features by specifying which settings to load to initialize the Django 
so that you can work with Django models and other features in a standalone script, 
which is outside of the typical request/response cycle of a Django web server. 
It's especially useful for tasks like data insertion, custom management commands, 
and scripts that need access to Django models and utilities.
'''

from demoApp.models import Student

## Using faker Module to Create Fake data for Insertion into Table
from faker import Faker

## Phone Numbers from Faker Class is NOT good
# Hence, we will Create our own random Phone No. Generator

from random import *
def phone_no_gen ():
    d = randint(6,9)
    num = str(d)
    for i in range(9):
        num = num + str(randint(0, 9))
    return int(num)

fake_obj = Faker()

## Generating random fake data using Faker class
def populate_data(n):
    for i in range(n):
        fname = fake_obj.name()
        froll_no = fake_obj.random_int(min=1, max=999)
        fdob = fake_obj.date()
        fmarks = fake_obj.random_int(min=0, max=100)
        femail = fake_obj.email()
        faddress = fake_obj.address()
        fphone_no = phone_no_gen()

        ## This Creates new data in the Table, else gets the existing data
        student_records = Student.objects.get_or_create(
            name = fname,
            roll_no = froll_no,
            dob = fdob,
            marks = fmarks,
            email = femail,
            address = faddress,
            phone_no = fphone_no
        )

## Here, populate function is used to Generate & Insert N students data
n = int(input('Enter a Number: '))
populate_data(n)

print(f'{n} Records Created Successfully ')