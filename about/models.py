from django.db import models
from cloudinary.models import CloudinaryField


class AboutUs(models.Model):
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    class Meta:
        verbose_name_plural = 'about us'


class ThingsWeOffer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'things we offer'
