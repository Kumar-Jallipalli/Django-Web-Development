from django.contrib import admin
from demoApp.models import Student

# Register your models here.
class StudentAdmin (admin.ModelAdmin):
    list_display = ['name', 'roll_no', 'dob', 'marks', 'phone_no', 'email', 'address']

admin.site.register(Student, StudentAdmin)