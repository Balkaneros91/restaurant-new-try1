# Generated by Django 3.2.18 on 2023-04-20 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(blank=True, upload_to='about_us'),
        ),
    ]
