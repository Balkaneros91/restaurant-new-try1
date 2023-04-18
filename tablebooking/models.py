from django.db import models
from django.contrib.auth.models import User

import datetime


class Table(models.Model):
    now = datetime.datetime.now()
    name = models.CharField(max_length=50, default='')
    capacity = models.IntegerField()
    opening_time = models.TimeField(default=datetime.time(11, 0))
    closing_time = models.TimeField(default=datetime.time(20, 0))

    def __str__(self):
        return f'Table {self.name} ({self.capacity} seats)'

    def is_available(self, date, time):
        reservations = Reservation.objects.filter(table=self, date=date, time__gte=time, time__lt=(time + datetime.timedelta(hours=2)))
        if reservations.exists():
            return False
        return time >= self.opening_time and (time + datetime.timedelta(hours=2)) <= self.closing_time and (time + datetime.timedelta(hours=2)) <= (self.closing_time - datetime.timedelta(hours=2))


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
    number_of_people = models.IntegerField(default=1)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} at {self.table} on {self.date} at {self.time}"


# class Booking(models.Model):
#     customer_name = models.CharField(max_length=255)
#     date = models.DateField()
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     table = models.ForeignKey(Table, on_delete=models.CASCADE)
#     number_of_people = models.IntegerField()
