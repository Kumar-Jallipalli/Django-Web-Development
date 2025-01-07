from django.shortcuts import render
from demoapp.forms import EmployeeForm

# Create your views here.
def employee_form_view (request):
    form = EmployeeForm()
    is_submitted = False
    name = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if (form.is_valid()):
            print("validation Successfull")
            name = form.cleaned_data['name']
            print('Submitted Employee Name: ', name)
            is_submitted = True
    my_dict = {'form': form, 'is_submitted': is_submitted, 'name': name}
    return render(request, 'demoapp/index.html', my_dict)
