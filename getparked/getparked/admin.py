from django.contrib import admin
from .models import Park, Customer, Booking

to_register = [Park, Customer, Booking]

for table in to_register:
    admin.site.register(table)
