from django.db import models


class AboutUs(models.Model):
    restaurant_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='about_us', blank=True)

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'
