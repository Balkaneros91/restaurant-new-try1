# Generated by Django 3.2.18 on 2023-04-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_booking', '0017_auto_20230428_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
