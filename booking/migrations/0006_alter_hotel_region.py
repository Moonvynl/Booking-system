# Generated by Django 5.0.2 on 2024-03-19 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_room_is_booked_alter_hotel_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='region',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking.region'),
        ),
    ]
