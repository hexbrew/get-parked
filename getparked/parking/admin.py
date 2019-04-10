from django.contrib import admin

from .models import DAYS
from .models import Customer, Lot, Bay, Booking, BookingDay
from .forms import LotAddForm 


class BayInline(admin.TabularInline):
    model = Bay
    list_display = ('code', 'size', 'occupancy_percentage', 'notes',)
    fields = ('code', 'size', 'occupancy_percentage', 'notes', 'bookings')
    readonly_fields = ('occupancy_percentage', 'bookings',)
    extra = 0


class BookingDayInline(admin.TabularInline):
    model = BookingDay
    extra = 0
    max_num = DAYS.__len__()


class BookingInline(admin.TabularInline):
    model = Booking
    # formset = BookingDaysFormset
    # form = BookingInlineForm
    extra = 0

    # fields = ('get_email', 'customer', 'monthly_rate')
    # readonly_fields = ('get_email', 'customer.user.email', 'bookings',)

    # def get_email(self, obj):
    #     return obj.customer.user.email


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_date',)
    search_fields = ('customer',)
    inlines = [
        BookingDayInline
    ]

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return BookingAddForm
        else:
            return super(BookingAdmin, self).get_form(request, obj, **kwargs)


@admin.register(Lot)
class LotAdmin(admin.ModelAdmin):
    list_display = ('location', 'monthly_rate', 'occupancy_percentage',)
    search_fields = ('location',)

    def add_view(self, request):
        self.inlines = []
        return super(LotAdmin, self).add_view(request)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.inlines = [BookingInline]
        return super(LotAdmin, self).change_view(request, object_id)

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return LotAddForm
        else:
            return super(LotAdmin, self).get_form(request, obj, **kwargs)
