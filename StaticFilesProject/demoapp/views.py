from django.shortcuts import render

# Create your views here.
def index_view (request):
    return render(request, 'demoapp/index.html')

def movies_view (request):
    main_msg = 'Movies News'
    sub_msg1 = "GAME CHANGER movie's trailer will release on Dec 29th"
    sub_msg2 = "Daaku Maharaj movie's prerelease evenet is on Dec 28th"
    sub_msg3 = "Pushpa 2 is going to dethrone Baahubali 2 Collections"
    sub_msg4 = "RRR2 movie is happening"
    my_dict = {
        'main_msg' : main_msg,
        'sub_msg1' : sub_msg1,
        'sub_msg2' : sub_msg2,
        'sub_msg3' : sub_msg3,
        'sub_msg4' : sub_msg4
    }
    return render(request, 'demoapp/app.html', my_dict)

def sports_view (request):
    main_msg = 'Sports News'
    sub_msg1 = "AUS vs IND Test - IND is about to lose the series"
    sub_msg2 = "WWE streaming rights were taken up by NETFLIX"
    sub_msg3 = "IPL 2025 will start from Mar 25"
    sub_msg4 = "Tennis world cup will start in January"
    my_dict = {
        'main_msg' : main_msg,
        'sub_msg1' : sub_msg1,
        'sub_msg2' : sub_msg2,
        'sub_msg3' : sub_msg3,
        'sub_msg4' : sub_msg4
    }
    return render(request, 'demoapp/app.html', my_dict)