from django import forms
from .models import Table, Reservation


class ReservationForm(forms.ModelForm):
    table = forms.ModelChoiceField(queryset=Table.objects.all(), empty_label=None)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Reservation
        fields = ('table', 'date', 'time', 'special_requests')
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 5})
        }
