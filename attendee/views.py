from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from pagination import CustomPagination
from .serializer import AttendeeSerializer
from .models import Attendee
# Create your views here.

class AttendeeViewSet(ModelViewSet):
    queryset = Attendee.objects.select_related('photo').all()
    serializer_class = AttendeeSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['role', 'email', 'phone_number']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name', 'last_name']
    ordering = ['-photo__photo_uploaded_at']


    #manual filtering based on role query parameter without using django-filter package
    # def get_queryset(self):
    #     queryset = Attendee.objects.select_related('photo').all()
    #     role = self.request.query_params.get('role')
    #     if role is not None:
    #         queryset = queryset.filter(role=role)
    #     return queryset
