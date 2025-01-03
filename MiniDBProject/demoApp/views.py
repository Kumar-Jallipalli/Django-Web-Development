from django.shortcuts import render
from demoApp.models import employeeTable

# Create your views here.
def emp_data_view (request):
    empdata = employeeTable.objects.all()
    my_dict = {'empdata': empdata}
    return render(request, 'demoApp/inde.html', my_dict)