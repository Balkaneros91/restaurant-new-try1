# Generated by Django 3.2.18 on 2023-04-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_auto_20230420_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThingsWeOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={},
        ),
    ]
