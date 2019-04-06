from django.db import models


class CarPark(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    total_parks = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)


class ReservedBay(models.Model):
    class Meta:
        unique_together = ('car_park_id', 'bay_id')

    bay_id = models.CharField(max_length=10, primary_key=True)  # id is char because could be C1, C10, A2, etc.
    car_park_id = models.ForeignKey(CarPark, on_delete=models.CASCADE)

    def __str__(self):
        return '{}\n car park: {}'.format(self.car_park_id, self.bay_id)


class Booking(models.Model):
    # Weak-ass entity
    id = models.AutoField(primary_key=True)
    car_park_id = models.ForeignKey(CarPark, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bay_id = models.OneToOneField(ReservedBay, null=True, blank=True, on_delete=models.CASCADE, default=None)

    # weekdays_booked = models.BinaryField(7, default=0b1111111)  # 7 bits represent Monday-Sunday, 1 for booked 0 for not
    # Don't work does it?

    def __str__(self):
        return '{}'.format(self.car_park_id)

# a view to say how many parks are still available on which days of the week
