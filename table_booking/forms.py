from django import forms
from django.core.exceptions import ValidationError
from .models import Booking
from .widget import DatePickerInput
from django.utils import timezone


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'number_of_guests', 'reservation_date_and_time', 'notes')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'number_of_guests': forms.NumberInput(attrs={'min': 1, 'max': 8}),
            'reservation_date_and_time': DatePickerInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Enter any special request'}),
        }

    def clean_number_of_guests(self):
        number_of_guests = self.cleaned_data.get('number_of_guests')
        if number_of_guests <= 0:
            raise ValidationError('Number of guests must be greater than zero')
        elif number_of_guests and number_of_guests > 8:
            raise forms.ValidationError("Please call or email for parties larger than 8")
        else:
            return number_of_guests

    def clean_reservation_date_and_time(self):
        reservation_date_and_time = self.cleaned_data.get('reservation_date_and_time')
        if reservation_date_and_time < timezone.now():
            raise ValidationError('Reservation date and time cannot be in the past')
        return reservation_date_and_time


class ApproveTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('name', 'email', 'phone', 'number_of_guests', 'reservation_date_and_time', 'notes', 'table', 'approved')
        widgets = {
            'name': forms.TextInput(attrs={'disabled': True}),
            'email': forms.EmailInput(attrs={'disabled': True}),
            'phone': forms.TextInput(attrs={'disabled': True}),
            'number_of_guests': forms.TextInput(attrs={'disabled': True}),
            'reservation_date_and_time': forms.DateInput(attrs={'type': 'date', 'disabled': True}),
            'notes': forms.Textarea(attrs={'rows': 2, 'disabled': True}),
            'table': forms.Select(attrs={'rows': 1}),
            'approved': forms.CheckboxInput(),
        }
