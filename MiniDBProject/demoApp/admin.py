from django.contrib import admin
from demoApp.models import employeeTable

# Register your models here.
class employeeAdmin (admin.ModelAdmin):
    list_display = ['eNo', 'eName', 'eSal', 'eAdd']

admin.site.register(employeeTable, employeeAdmin)