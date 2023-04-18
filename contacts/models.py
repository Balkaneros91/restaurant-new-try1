from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
