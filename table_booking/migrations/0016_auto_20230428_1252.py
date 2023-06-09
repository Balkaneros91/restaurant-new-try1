# Generated by Django 3.2.18 on 2023-04-28 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table_booking', '0015_alter_booking_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='table_assigned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='table_booking.table'),
        ),
    ]
