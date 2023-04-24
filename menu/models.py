from django.db import models
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(blank=True, null=False, upload_to='menu/')
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(MenuItem, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'menu item'
        verbose_name_plural = 'menu items'

    def __str__(self):
        return self.name
