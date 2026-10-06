from django.contrib import admin
from django.utils.html import format_html
from .models import Attendee, Attendee_photo


# Register your models here.
class AttendeePhotoInline(admin.TabularInline):
    model = Attendee_photo
    readonly_fields = ['thumbnail']
    extra = 1

    def thumbnail(self, instance):
        if instance.photo.name != '':
            return format_html('<img src="{}" class = "thumbnail" />', instance.photo.url)
        return 'No image'




@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'attendee_code',
                    'phone_number', 'email', 'organization', 'role')
    inlines = [AttendeePhotoInline]
    list_per_page = 10
    ordering = ('first_name', 'last_name')
    list_filter = ('role',)
    search_fields = ('first_name__istartswith', 'last_name__istartswith')


    class Media:
            css = {
                'all': ['attendee/styles.css']
            }