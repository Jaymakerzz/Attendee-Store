import re
from django import forms
from attendee.models import Attendee, Attendee_photo


class NewAttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['first_name', 'last_name', 'email',
                  'phone_number', 'organization', 'role']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form__input form__input--text',
                                                 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form__input form__input--text',
                                                'placeholder': 'Last name'}),
            'email': forms.EmailInput(attrs={
                'class': 'form__input form__input--text', 
                'placeholder': 'Email'
                }),
            'phone_number': forms.TextInput(attrs={
                'type': 'tel',
                'class': 'form__input', 
                'placeholder': 'Phone number'
                }),
            'organization': forms.TextInput(attrs={'class': 'form__input',
                                                   'placeholder': 'Organization'}),
            'role': forms.Select(attrs={'class': 'form__input'}),
        }
        labels = {
            "role": "",
        }

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
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form__file'}),
        }
        labels = {
                    "photo": "Upload image",
                }