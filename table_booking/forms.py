from django import forms
from .models import Booking, Table

from django.utils import timezone


class BookingTableForm(forms.ModelForm):
    class Meta:
        model = Booking
        # fields = '__all__'
        fields = ('name', 'email', 'phone', 'number_of_guests', 'date', 'reservation_time', 'notes', 'table')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 2}),
        }


# class BookingTableForm(forms.ModelForm):
#     table = forms.ModelChoiceField(queryset=Table.objects.all(), empty_label='Select a table')
#     name = forms.CharField(max_length=50, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(max_length=30, required=True)
#     number_of_guests = forms.IntegerField(min_value=1, max_value=8, required=True)
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
#     # date = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}), input_formats=['%Y-%m-%dT%H:%M'])
#     reservation_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
#     notes = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

#     class Meta:
#         model = Booking
#         fields = ('name', 'email', 'phone', 'number_of_guests', 'date', 'reservation_time', 'notes')
#         widgets = {
#             'date': forms.DateInput(attrs={'type': 'date'}),
#             'reservation_time': forms.TimeInput(attrs={'type': 'time'}),
        # }

    # def clean_date(self):
    #     date = self.cleaned_data.get('date')
    #     if date < timezone.localdate():
    #         raise forms.ValidationError("Cannot book for past dates.")
    #     return date

    # def __init__(self, table_id, *args, **kwargs):
    #     super(BookingTableForm, self).__init__(*args, **kwargs)
    #     table = Table.objects.get(id=table_id)
    #     self.fields['reservation_time'].choices = [(choice, choice) for choice in table.available_times]
