from django.shortcuts import render
from demoApp.models import Student

# Create your views here.
def student_data_view (request):
    data = Student.objects.all()
    my_dict = {'data': data}
    return render(request, 'demoApp/Index.html', my_dict)