from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def student_form_view (request):
    ## Create Form Object
    form_obj = StudentForm()
    my_dict = {'form': form_obj}
    return render(request, 'testapp/index.html', my_dict)