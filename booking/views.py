from django.shortcuts import render, redirect
from booking.models import *
from django.http import HttpResponse
from django.contrib.auth import logout
from datetime import datetime



def logout_view(request):
    logout(request)
    return redirect('home')

def home(request):
    regions = Region.objects.all()

    context = {
        "regions": regions
    }

    return render(
        request,
        "booking/main.html",
        context,
    )


def get_hotels_by_region(request, pk):
    hotels = Hotel.objects.filter(region = pk)

    context = {
        "hotels": hotels
    }

    return render(
        request,
        "booking/hotels_list.html",
        context,
    )

def get_rooms_by_hotel(request, pk):
    rooms = Room.objects.filter(hotel = pk)
    

    context = {
        "rooms": rooms,
    }

    return render(
        request,
        "booking/rooms_list.html",
        context,
    )


def book_room(request, pk):
    if request.method == "POST":
        user = request.user
        if user.is_anonymous:
            return HttpResponse(
                'You need to be logged in to book a room!',
                status = 400
            )
        start_time = request.POST.get('start-time')
        end_time = request.POST.get('end-time')

        try:
            room = Room.objects.get(id = pk)
        except ValueError:
            return HttpResponse(
                'Wrong value for room number!',
                status = 400
            )
        except Room.DoesNotExist:
            return HttpResponse(
                'This room doesnt exists',
                status = 400
            )
        
        booking = Booking.objects.create(
            user = user,
            room = room,
            start_time = start_time,
            end_time = end_time,
        )
        return redirect("booking-details", pk = booking.id)
    else:
        return render(
            request,
            "booking/booking_form.html"
        )

def booking_details(request, pk):
    try:
        booking = Booking.objects.get(id = pk)
        context = {
            "booking": booking
        }

        return render(
            request,
            "booking/booking_details.html",
            context
        )
    except Booking.DoesNotExist:
        return HttpResponse(
            'This booking doesnt exists',
            status = 400
        )

def room_details(request, pk):
    try:
        room = Room.objects.get(id = pk)
        context = {
            "room": room
        }

        return render(
            request,
            "booking/room_details.html",
            context
        )
    except Room.DoesNotExist:
        return HttpResponse(
            'This room doesnt exists',
            status = 400
        )


