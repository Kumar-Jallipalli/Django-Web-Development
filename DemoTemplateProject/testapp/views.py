from django.shortcuts import render

# Create your views here.
def template_view(request):
    return render(request, 'testapp/index.html')
    ## From the above code, 
    ## for the that particular request argument, 
    ## render() fn will 1st access the template defined inside 'testapp', render it & send that as HTTP Response 
    ## 'testapp/index.html' -> we have given this as file path, 
    ## Since upto `templates` folder path location is defined in 'settings.py'
    ## So, Django will know this file even if we give path like this 'testapp/index.html'