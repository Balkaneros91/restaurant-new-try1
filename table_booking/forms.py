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
            if number_of_guests <= 0:
                raise ValidationError('Number of guests must be greater than zero')
            elif number_of_guests and number_of_guests > 8:
                raise forms.ValidationError("Please call or email for parties larger than 8")
            else:
                return number_of_guests

        def clean_number_of_guests(self):
            number_of_guests = self.cleaned_data.get('number_of_guests')
            if number_of_guests is None:
                raise ValidationError('Please enter a valid number of guests')

            if number_of_guests <= 0:
                raise ValidationError('Number of guests must be greater than zero')

            if number_of_guests > 8:
                raise ValidationError('Sorry, we cannot accommodate parties larger than 8 guests')

            return number_of_guests

        def clean(self):
            cleaned_data = super().clean()
            reservation_date = cleaned_data.get('reservation_date')
            reservation_time = cleaned_data.get('reservation_time')
            now = timezone.now()

            if reservation_date is not None and reservation_time is not None:
                reservation_datetime = timezone.make_aware(
                    timezone.datetime.combine(reservation_date, reservation_time),
                    timezone.get_current_timezone()
                )
                if reservation_datetime < now:
                    raise ValidationError('Reservation date and time cannot be in the past')
                elif reservation_datetime - now < timezone.timedelta(minutes=30):
                    raise ValidationError('Reservation must be made at least 30 minutes in advance')
            return cleaned_data
