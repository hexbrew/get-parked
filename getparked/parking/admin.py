from django.contrib import admin

# Register your models here.
from .models import Customer, Lot, LotDay, Booking


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_date',)
    search_fields = ('customer',)


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('location', 'bays', 'occupancy_percentage', 'daily_rate')
    search_fields = ('location',)


@admin.register(LotDay)
class LotDayAdmin(admin.ModelAdmin):
    list_display = ('lot','day', 'rate', 'occupancy_percentage')
    search_fields = ('lot',)
