from django.db import models


class CarMake(models.Model):
    """
    Model representing the make (manufacturer) of a car
    """
    name = models.CharField('Car make', blank=False)


class CarModel(models.Model):
    """
    Model representing the model of a car
    """
    name = models.CharField('Car model', blank=False)
    make = models.ForeignKey('CarMake', blank=False)


class Car(models.Model):
    """
    Model representing an individual car
    """
    model = models.ForeignKey('CarModel', blank=False)

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
