from django.db import models
from datetime import timedelta
from django.core.validators import MinValueValidator


class CarMake(models.Model):
    """
    Model representing the make (manufacturer) of a car
    """
    name = models.CharField('Car make', max_length=100, blank=False)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """
    Model representing the model of a car
    """
    name = models.CharField('Car model', max_length=100, blank=False)
    make = models.ForeignKey('CarMake', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Car(models.Model):
    """
    Model representing an individual car
    """
    model = models.ForeignKey('CarModel', blank=False, on_delete=models.CASCADE)

    registration = models.CharField(
        'Registration number',
        max_length=7,
        help_text="Enter car's registration number (no spaces)"
    )

    vin = models.CharField(
        'VIN',
        max_length=17,
        help_text="Vehicle identification number"
    )

    def __str__(self):
        return f'{self.model.name}: {self.registration}'


class Booking(models.Model):
    """
    Model representing a booking made for a car
    """
    car = models.ForeignKey('Car', blank=False, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    release_time = models.DateTimeField()
    duration_hrs = models.IntegerField(
        'Duration',
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Rental duration in hours"
    )

    def __str__(self):
        return f'Booking id: {self.id}'

    def save(self, *args, **kwargs):
        self.end_time = self.start_time + timedelta(hours=self.duration_hrs)
        self.release_time = self.end_time + timedelta(hours=2)

        super(Booking, self).save(*args, **kwargs)
