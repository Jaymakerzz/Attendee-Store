from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'attendee'

router = DefaultRouter()
router.register(r'attendees', views.AttendeeViewSet, basename='attendee')
# router.register(r'register', views.RegisterAttendee, basename='registered')

urlpatterns = [
    path('', include(router.urls), name="attendee"),
]