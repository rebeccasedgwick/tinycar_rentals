from django.contrib import admin
from rentals.models import CarMake, CarModel, Car, Booking
from rentals.forms import BookingForm

admin.site.register(CarMake)


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'registration', 'vin')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'start_time', 'end_time', 'release_time')
    form = BookingForm
