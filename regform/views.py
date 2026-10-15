from django.shortcuts import render
from .forms import NewAttendeeForm, NewAttendeePhotoForm

# Create your views here.

def index(request):
    return render(request, 'register/index.html')

def attendees(request):
    if request.method == 'POST':
        attendee_form = NewAttendeeForm(request.POST)
        photo_form = NewAttendeePhotoForm(request.POST, request.FILES)
        has_photo = bool(request.FILES.get("photo"))

        attendee_valid = attendee_form.is_valid()
        photo_valid = photo_form.is_valid() if has_photo else True

        if attendee_valid and photo_valid:
            attendee = attendee_form.save()
            photo = photo_form.save(commit=False)
            photo.attendee = attendee
            photo.save()
            return index(request)
    else:
        attendee_form = NewAttendeeForm()
        photo_form = NewAttendeePhotoForm()

    return render(request, 'register/attendee.html', {
        'attendee': attendee_form,
        'photo': photo_form,

    })