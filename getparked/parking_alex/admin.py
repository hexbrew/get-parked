from django.contrib import admin
from .models import CarPark, Customer, Booking, ReservedBay

to_register = [CarPark, Customer, Booking, ReservedBay]

for table in to_register:
    admin.site.register(table)
