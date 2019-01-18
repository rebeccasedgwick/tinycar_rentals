from django import forms
from rentals.models import Booking
from django.core.exceptions import ValidationError
from datetime import timedelta


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('car', 'start_time', 'duration_hrs')

    def clean(self, *args, **kwargs):
        data = self.cleaned_data

        end_time = data['start_time'] + timedelta(hours=data['duration_hrs'])
        release_time = end_time + timedelta(hours=2)

        cars_taken = Booking.objects.filter(
            car=data['car'],
            start_time__range=(data['start_time'], release_time),
            end_time__range=(data['start_time'], release_time)
        ).count()

        if cars_taken > 0:
            raise ValidationError('This car is not available for the selected time and duration')

        return data
