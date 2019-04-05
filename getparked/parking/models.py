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
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday'),
)


class Customer(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name=_('customer'), null=False, blank=False)

    def __str__(self):
        return str(self.user)

    def __unicode__(self):
        return str(self.user)


class Lot(models.Model):
    location = models.CharField(
        unique=True, null=False, blank=False, max_length=300)
    bays = models.IntegerField(null=False, blank=False)
    daily_rate = models.FloatField(null=False, blank=False, default=0)

    def occupancy(self):
        percentage = 0
        for day in self.days.all():
            percentage += day.occupancy()/self.days.count()
        return percentage

    def occupancy_percentage(self):
        return f"{round(self.occupancy())}%"

    def __str__(self):
        return self.location

    def __unicode__(self):
        return self.location


class LotDay(models.Model):
    lot = models.ForeignKey(
        to=Lot, on_delete=models.CASCADE, related_name=_('days'), null=False, blank=False)
    day = models.CharField(
        choices=DAYS, max_length=3, null=False, blank=False, default=DAYS[0][0])
    rate = models.FloatField(null=False, blank=False)

    class meta:
        constraints = [
            models.UniqueConstraint(fields=['lot', 'day'], name='unique_day')
        ]

    def occupancy(self):
        return self.bookings.count()/self.lot.bays*100

    def occupancy_percentage(self):
        return f"{round(self.occupancy())}%"

    def __str__(self):
        return f"{self.lot} ({self.day})"

    def __unicode__(self):
        return f"{self.lot} ({self.day})"


class Booking(models.Model):
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE, related_name=_('booking'), null=False, blank=False)
    days = models.ManyToManyField(
        to=LotDay, related_name=_('bookings'))
    start_date = models.DateField(auto_now=True, null=False)

    def weekly_rate(self):
        total = 0
        for day in self.days.all():
            total += day.rate
        return total

    def monthly_rate(self):
        # Charge for 4 weeks per month
        return self.weekly_rate() * 4

    def lots(self):
        lots = set()
        for day in self.days.all():
            lots.add(day.lot)
        return lots

    def __str__(self):
        return f"{self.customer}: {self.start_date}"

    def __unicode__(self):
        return f"{self.customer}: {self.start_date}"


@receiver(post_save, sender=Lot, dispatch_uid="lot_created")
def create_days(sender, instance, created, **kwargs):
    """
    Create LotDay entries for newly created lots.
    """
    if not created:
        # Not relevant
        return

    for day in DAYS:
        LotDay.objects.create(
            lot=instance, day=day[0], rate=instance.daily_rate)


@receiver(m2m_changed, sender=Booking.days.through, dispatch_uid="booking_days_changed")
def booking_days_changed(sender, instance, action, **kwargs):
    """
    Delete a new booking if it is not valid.
    """
    if action != "post_add":
        # Not relevant
        return

    for day in instance.days.all():
        if day.bookings.count() > day.lot.bays:
            # This booking overfills the number of bays, delete it and stop
            instance.delete()
            return
