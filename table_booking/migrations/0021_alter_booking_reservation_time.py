# Generated by Django 3.2.18 on 2023-04-28 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('table_booking', '0020_auto_20230428_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='reservation_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
