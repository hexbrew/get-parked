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

    def used_bays(self):
        used = 0
        bays = self.bays.all()
        for bay in bays:
            if bay.occupancy() > 0:
                used += 1

        return used

    def __str__(self):
        return self.location

    def __unicode__(self):
        return self.location


class Bay(models.Model):
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE,
                            related_name=_('bays'), null=False, blank=False)
    number = models.PositiveSmallIntegerField(null=False, blank=False, default=1, help_text="A lot-specific bay number.")
    reservation_code = models.CharField(
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
            if d.day == day[0]:
                return True

        return False

    def get_day_booking(self, day):
        """
        Given a day value (from DAYS) return the booking for that day, if one exists.
        """
        for d in self.days.all():
            if d.day == day[0]:
                return d.booking

        return None

    def bookings(self):
        """
        Returns the customer bookings for this bay.
        """
        bookings = []
        for day in self.days.all():
            bookings.append(day.booking)
        return bookings

    def __str__(self):
        return f"{self.number}"

    def __unicode__(self):
        return f"{self.number}"


class Booking(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE, related_name=_('bookings'), null=False, blank=False)
    lot = models.ForeignKey(to=Lot, on_delete=models.CASCADE,
                            related_name=('bookings'), null=False, blank=False)
    monthly_rate = models.FloatField(null=False, blank=False, default=0)
    start_date = models.DateField(auto_now=True, null=False)

    def get_unique_bays(self):
        bays = set()
        for day in self.days.all():
            bays.add(day.bay)
        return bays

    def __str__(self):
        return f"{self.customer}"

    def __unicode__(self):
        return f"{self.customer}"


class BookingDay(models.Model):
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name=_('days'), null=False, blank=False)
    day = models.CharField(
        choices=DAYS, max_length=3, null=False, blank=False, default=DAYS[0][0])
    bay = models.ForeignKey(Bay, on_delete=models.CASCADE, related_name=_('days'),
                            null=False, blank=False)
