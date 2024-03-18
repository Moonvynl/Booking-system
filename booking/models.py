from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Region(models.Model):
    name = models.CharField(max_length = 63)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Hotel(models.Model):
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name = "hotels", default='default region value')
    name = models.CharField(max_length = 63)
    img = models.ImageField(upload_to = "hotels", default='img/default_image.jpg')
    rating = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length = 63)
    description = models.TextField()

    class Meta():
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = "rooms")
    number = models.CharField(max_length = 63)
    img = models.ImageField(upload_to = "rooms", default='img/default_image.jpg')
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f"Room - {self.number}"
    
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ["number"]


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = "bookings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = "bookings")

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.room} booked - by {self.user}"
    
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-end_time", "room"]
    
