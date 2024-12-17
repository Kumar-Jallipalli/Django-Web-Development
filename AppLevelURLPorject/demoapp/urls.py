from django.urls import path

## importing the views file from current package
from . import views

urlpatterns = [
    path('fisrt/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourt_view),
    path('fifth/', views.fifth_view),
]