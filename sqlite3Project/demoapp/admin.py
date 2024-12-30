from django.contrib import admin
from demoapp.models import Students

# Register your models here.
class StudentsAdmin (admin.ModelAdmin):
    list_display = ['name', 'marks']

admin.site.register(Students, StudentsAdmin)