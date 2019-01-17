from django.contrib import admin
from rentals.models import CarMake, CarModel, Car

admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Car)
# Register your models here.
