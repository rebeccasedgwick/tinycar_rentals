from django.db import models


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
        return self.vin
