from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.attendees, name='home'),
    path('attendees/', views.attendees, name='attendees'),
]