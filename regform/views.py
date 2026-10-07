from django.shortcuts import render
from .forms import NewAttendeeForm, NewAttendeePhotoForm

# Create your views here.

def index(request):
    return render(request, 'register/index.html')

def attendees(request):
    if request.method == 'POST':
        attendee_form = NewAttendeeForm(request.POST)
        if request.FILES:
            photo_form = NewAttendeePhotoForm(request.POST, request.FILES)
        else:
            photo_form = NewAttendeePhotoForm()

        if attendee_form.is_valid() or photo_form.is_valid():
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