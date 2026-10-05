from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'attendees', views.AttendeeViewSet, basename='attendee')

urlpatterns = [
    path('', include(router.urls)),
    path('attendees/', views.AttendeeViewSet.as_view({'get': 'list'}), name='attendee'),
]