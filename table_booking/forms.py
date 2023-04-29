from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from .widget import DatePickerInput, TimePickerInput

from django.utils import timezone


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'number_of_guests', 'reservation_date', 'reservation_time', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'number_of_guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'reservation_date': DatePickerInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reservation_time': TimePickerInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter any special request'}),
        }

        def clean_number_of_guests(self):
            number_of_guests = self.cleaned_data.get('number_of_guests')
            if number_of_guests is None:
                raise ValidationError('Please enter a valid number of guests')

            if number_of_guests <= 0:
                raise ValidationError('Number of guests must be greater than zero')

            if number_of_guests > 8:
                raise ValidationError('Sorry, we cannot accommodate parties larger than 8 guests')

            return number_of_guests
