from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


class Region(models.Model):
    name = models.CharField(max_length = 63)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Region"
        verbose_name_plural = "Regions"


class Hotel(models.Model):
    region = models.ForeignKey(Region, on_delete = models.CASCADE, related_name = "hotels", default = 1)
    name = models.CharField(max_length = 63)
    img = models.ImageField(upload_to = "hotel_imgs/", default='default.png')
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
    img = models.ImageField(upload_to = "room_imgs/", default='default.png')
    capacity = models.IntegerField()
    location = models.TextField()
    description = models.TextField()

    def is_booked(self):
        return Booking.objects.filter(room=self, end_time__gt=timezone.now()).exists()
    
    def booking_times(self):
        bookings = Booking.objects.filter(room=self)
        return [{'start_time': booking.start_time.strftime('%Y-%m-%d'), 'end_time': booking.end_time.strftime('%Y-%m-%d')} for booking in bookings]

    def booking_times_without_user(self, user):
        bookings = Booking.objects.filter(room=self).exclude(user=user)
        return [{'start_time': booking.start_time.strftime('%Y-%m-%d'), 'end_time': booking.end_time.strftime('%Y-%m-%d')} for booking in bookings]

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


