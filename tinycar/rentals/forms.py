from django import forms
from rentals.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('model', 'start_time', 'duration_hrs')
