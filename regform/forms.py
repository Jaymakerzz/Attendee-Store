import re
from django import forms
from attendee.models import Attendee, Attendee_photo


class NewAttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'organization', 'role']

    def clean_phone_number(self):
        phone = re.sub(r'\D', '', self.cleaned_data['phone_number'])
        if len(phone) < 9:
            raise forms.ValidationError('Enter a valid phone number.')
        phone = f"+255{phone[-9:]}"

        if Attendee.objects.filter(phone_number=phone).exists():
            raise forms.ValidationError('Phone number already exists.')
        return phone


class NewAttendeePhotoForm(forms.ModelForm):
    class Meta:
        model = Attendee_photo
        fields = ['photo']
