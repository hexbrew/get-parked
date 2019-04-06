from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import CarPark, Booking


# Create your views here.

def car_park_availability(request):
    car_park = CarPark.objects.all()[0]
    park_id = car_park.id
    capacity = car_park.total_parks
    used_parks = Booking.objects.filter(car_park_id=car_park)
    print('parks---')
    for park in used_parks:
        print(park)
    print('parks---')

    remaining_parks = capacity - len(used_parks)

    output = 'park: {}\n<br>capacity: {}\n<br>remaining: {}'.format(car_park, capacity, remaining_parks)

    print(output)
    return HttpResponse(output)
