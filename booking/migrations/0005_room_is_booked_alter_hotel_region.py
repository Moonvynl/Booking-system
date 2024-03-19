# Generated by Django 5.0.2 on 2024-03-19 15:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_hotel_options_alter_region_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='region',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking.region'),
        ),
    ]
