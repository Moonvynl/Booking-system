from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name = "home"),
    path('hotels/<int:pk>/', get_hotels_by_region, name = "hotels"),
    path('rooms/<int:pk>/', get_rooms_by_hotel, name = "rooms"),

    path('accounts/logout/', logout_view, name="logout"),
    path('book-room/<int:pk>/', book_room, name = "book-room"),
    path('booking-details/<int:pk>/', booking_details, name = "booking-details"),
    path('room-details/<int:pk>/', room_details, name = "room-details"),

    path('cabinet/', user_cabinet, name = "cabinet"),
    path('cabinet/delete-booking/<int:pk>/', delete_booking, name = "delete-booking"),
    path('cabinet/update-booking-time/<int:pk>/', update_booking_time, name = "update-booking-time"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)