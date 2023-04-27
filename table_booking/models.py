from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


# # Model for Table
class Table(models.Model):
    table_number = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50, default=2)

    def __str__(self):
        return f'Table - {self.table_number} for {self.capacity} guests.'


# Model for Booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=30, null=False, blank=True)
    number_of_guests = models.IntegerField(default=1)
    date = models.DateField()
    reservation_time = models.TimeField()
    notes = models.TextField(null=True, blank=True)

    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __str__(self):
        return f"Reservation for {self.name} at {self.reservation_time}"
