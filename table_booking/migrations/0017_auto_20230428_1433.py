# Generated by Django 3.2.18 on 2023-04-28 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table_booking', '0016_auto_20230428_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='table_assigned',
        ),
    ]
