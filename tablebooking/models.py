from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Table(models.Model):
    name = models.CharField(max_length=50, default='')
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer} reserved Table {self.table} on {self.date} at {self.time}"

    class Meta:
        unique_together = ('table', 'date', 'time')


class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} at {self.table} on {self.date} at {self.time}"
