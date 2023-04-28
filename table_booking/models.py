from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
STATUS = ((0, 'Pending'), (1, 'Booked'))


# # Model for Table
class Table(models.Model):
    table_number = models.CharField(max_length=50)
    capacity = models.CharField(max_length=50, default=2)

    def __str__(self):
        return f'Table - {self.table_number} for {self.capacity} guests.'


# Model for Booking
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=30, null=False, blank=True)
    number_of_guests = models.IntegerField(default=2)

    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    reservation_date_and_time = models.DateTimeField()
    notes = models.TextField(max_length=300, null=True, blank=True)

    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    table_assigned = models.BooleanField(default=False)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name

    def __str__(self):
        return f"Reservation for {self.name} at {self.reservation_date_and_time}"
