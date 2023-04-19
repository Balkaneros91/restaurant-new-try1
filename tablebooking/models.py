from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone


# class Table(models.Model):

#     name = models.CharField(max_length=100)
#     capacity = models.IntegerField()
#     is_available = models.BooleanField(default=True)

#     def __str__(self):
#         return f'Table {self.name} ({self.capacity} seats)'


# class Customer(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()


class Booking(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # table = models.ForeignKey(Table, on_delete=models.CASCADE)
    # date = models.DateField()
    # time = models.TimeField()
    # party_size = models.IntegerField()
    # created_at = models.DateTimeField(default=timezone.now)
    # special_requests = models.TextField(null=True, blank=True)

    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=30, null=False, blank=True)
    # number_of_p = models.IntegerField()
    number_of_p = models.PositiveIntegerField(default=1)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name
        # return f"{self.customer} at {self.table} on {self.date} at {self.time}"
