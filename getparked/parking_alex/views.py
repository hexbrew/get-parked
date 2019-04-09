from django.shortcuts import render
from django.http import HttpResponse
import datetime

from .models import CarPark, Booking


# Create your views here.

def car_park_availability(request):
    car_park = CarPark.objects.all()[0]

    output = f'remaining: {car_park.remaining_unreserved_count()}'

    return HttpResponse(output)
