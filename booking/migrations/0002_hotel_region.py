# Generated by Django 5.0.2 on 2024-03-18 18:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('rating', models.IntegerField()),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=63)),
                ('description', models.TextField()),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='booking.room')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('hotels', models.ManyToManyField(related_name='regions', to='booking.hotel')),
            ],
        ),
    ]