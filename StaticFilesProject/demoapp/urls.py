from django.urls import path
from demoapp import views

urlpatterns = [
    path('', views.index_view),
    path('movies/', views.movies_view),
    path('sports/', views.sports_view),
]