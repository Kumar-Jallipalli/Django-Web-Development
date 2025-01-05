from django.shortcuts import render
from demoapp.forms import FeedbackForm

# Create your views here.
def feedback_form_view (request):
    is_submitted = False
    s_feedback = ''
    if (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        if (form.is_valid()):
            print("Name :", form.cleaned_data['name'])
            print("roll_no :", form.cleaned_data['roll_no'])
            print("email :", form.cleaned_data['email'])
            print("feedback :", form.cleaned_data['feedback'])
            is_submitted = True
            s_feedback = form.cleaned_data['feedback']
    form = FeedbackForm()
    my_dict = {'form': form, 'submitted': is_submitted, 'feedback': s_feedback}
    return render(request, 'demoapp/Index.html', my_dict)
