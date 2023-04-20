from django.db import models
from cloudinary.models import CloudinaryField


class AboutUs(models.Model):
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    # image = models.ImageField(upload_to='about_us', blank=True)

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'
