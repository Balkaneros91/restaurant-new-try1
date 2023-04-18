from django.db import models


class AboutUs(models.Model):
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField()
