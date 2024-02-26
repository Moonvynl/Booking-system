from django.shortcuts import render
from booking.models import *


def get_rooms_list(request):
    rooms = Room.objects.all()

    context = {
        "rooms": rooms
    }

    return render(
        request,
        "booking/rooms_list.html",
        context,
    )

def get_users_list(request):
    users = User.objects.all()

    context = {
        "users": users
    }

    return render(
        request,
        "booking/users_list.html",
        context,
    )