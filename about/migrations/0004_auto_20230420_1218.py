# Generated by Django 3.2.18 on 2023-04-20 12:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_alter_aboutus_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='image',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]