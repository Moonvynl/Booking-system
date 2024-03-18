from django.contrib import admin
from booking.models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Region)
admin.site.register(Hotel)