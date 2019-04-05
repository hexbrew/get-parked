from django.db import models


class CarPark(models.Model):
    name = models.CharField(200)
    address = models.CharField(200)
    total_parks = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(200)


class ReservedBay(models.Model):
    BayId = models.CharField(primary_key=True)  # id is char because could be C1, C10, A2, etc.
    CarParkID = models.ForeignKey(CarPark, primary_key=True, on_delete=models.CASCADE)


class Booking(models.Model):
    CarParkID = models.ForeignKey(CarPark, primary_key=True, on_delete=models.CASCADE)
    customerID = models.ForeignKey(Customer, primary_key=True, on_delete=models.CASCADE)
    bay = models.ForeignKey(ReservedBay, primary_key=True, null=True, on_delete=models.CASCADE)  # if Null, not a specific bay
    # days of the week

# a view to say how many parks are still available on which days of the week
