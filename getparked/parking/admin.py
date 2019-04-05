from django.contrib import admin

# Register your models here.
from .models import Customer, Lot, LotDay, Booking


class LotDayInline(admin.TabularInline):
    model = LotDay

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


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
    inlines = [
        LotDayInline
    ]
