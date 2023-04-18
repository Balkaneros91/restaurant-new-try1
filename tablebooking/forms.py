from django import forms
from django.utils import timezone
from .models import Booking


class BookingForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'number_of_people']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }

    def clean(self):
        cleaned_data = super().clean()
        table = cleaned_data.get('table')
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        if table is None or date is None or time is None:
            raise forms.ValidationError("Table, date, and time fields are required.")

        # Check if the selected time is within the opening and closing hours
        if time < table.opening_time or time > table.closing_time:
            raise forms.ValidationError("This table is not available for the selected time.")

        # Check if the selected time is at least 2 hours before the closing time
        if table.closing_time - time <= timezone.timedelta(hours=2):
            raise forms.ValidationError("Reservation must be made at least 2 hours before the closing time.")

        # Check if there are any conflicting reservations for the selected table, date and time
        conflicting_reservations = table.reservation_set.filter(date=date, time=time)

        if conflicting_reservations.exists():
            raise forms.ValidationError("This table is already reserved for the selected date and time.")

        total_people = cleaned_data.get('number_of_people')
        if total_people < 1:
            raise forms.ValidationError("Number of people must be greater than zero.")

        return cleaned_data
