from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

DAYS = (
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
)


class Customer(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name=_('customer'), null=False, blank=False)

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)


class Lot(models.Model):
    location = models.CharField(
        unique=True, null=False, blank=False, max_length=300)
    monthly_rate = models.FloatField(null=False, blank=False, default=0)

    def occupancy(self):
        """
        Returns a fractional occupancy value for this bay.
        """
        fraction = 0
        for bay in self.bays.all():
            fraction += bay.occupancy()/self.bays.count()
        return fraction

    def occupancy_percentage(self):
        return f"{round(self.occupancy()*100)}%"

    def bookings(self):
        bookings = set()
        bays = self.bays.all()
        for bay in bays:
            booking_days = bay.days.all()
            for day in booking_days:
                bookings.add(day.booking)

        return bookings


    def __str__(self):
        return self.location

    def __unicode__(self):
        return self.location


class Bay(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE,
                            related_name=_('bays'), null=False, blank=False)
    code = models.CharField(
        max_length=5, null=True, blank=True, help_text="A lot-specific code to use for reserved bays. This should not be set on non-reserved bays.")  # For reserved bays
    size = models.CharField(max_length=10, null=False,
                            blank=False, default='Any')
    notes = models.CharField(max_length=255, null=True, blank=True)

    def occupancy(self):
        """
        Returns a fractional occupancy value for this bay.
        """
        return self.days.count() / DAYS.__len__()

    def occupancy_percentage(self):
        return f"{round(self.occupancy()*100)}%"

    def is_occupied(self, day):
        """
        Given a day value (from DAYS) return whether this bay is occupied for that day.
        """
        for d in self.days.all():
            if d.day == day:
                return True

        return False

    def bookings(self):
        """
        Returns the customer bookings for this bay.
        """
        bookings = []
        for day in self.days.all():
            bookings.append(day.booking)
        return bookings

    def __str__(self):
        return f"{self.lot} ({self.code or 'Virtual'})"

    def __unicode__(self):
        return f"{self.lot} ({self.code or 'Virtual'})"


class Booking(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE, related_name=_('bookings'), null=False, blank=False)
    monthly_rate = models.FloatField(null=False, blank=False, default=0)
    start_date = models.DateField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.customer}: {self.start_date}"

    def __unicode__(self):
        return f"{self.customer}: {self.start_date}"


class BookingDay(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name=_('days'), null=False, blank=False)
    day = models.CharField(
        choices=DAYS, max_length=3, null=False, blank=False, default=DAYS[0][0])
    bay = models.ForeignKey(Bay, on_delete=models.CASCADE, related_name=_('days'),
                            null=False, blank=False)


# @receiver(post_save, sender=Lot, dispatch_uid="lot_created")
# def create_days(sender, instance, created, **kwargs):
#     """
#     Create LotDay entries for newly created lots.
#     """
#     if not created:
#         # Not relevant
#         return

#     for day in DAYS:
#         LotDay.objects.create(
#             lot=instance, day=day[0], rate=instance.daily_rate)


# @receiver(m2m_changed, sender=Booking.days.through, dispatch_uid="booking_days_changed")
# def booking_days_changed(sender, instance, action, **kwargs):
#     """
#     Delete a new booking if it is not valid.
#     """
#     if action != "post_add":
#         # Not relevant
#         return

#     for day in instance.days.all():
#         if day.bookings.count() > day.lot.bays:
#             # This booking overfills the number of bays, delete it and stop
#             instance.delete()
#             return
