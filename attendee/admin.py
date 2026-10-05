from django.contrib import admin
from .models import Attendee, Attendee_photo

# Register your models here.
class AttendeePhotoInline(admin.TabularInline):
    model = Attendee_photo
    extra = 1


@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'attendee_code',
                    'phone_number', 'email', 'organization', 'role')
    inlines = [AttendeePhotoInline]
    list_per_page = 10
    ordering = ('first_name', 'last_name')
    list_filter = ('role',)
    search_fields = ('first_name__istartswith', 'last_name__istartswith')
