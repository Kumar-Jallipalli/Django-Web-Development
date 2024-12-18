from django.shortcuts import render
from datetime import datetime

# Create your views here.
def date_view(request):
    date = datetime.now()
    my_dict = {'dt':date}
    return render(request, 'testapp/index.html', {'dt':date} )