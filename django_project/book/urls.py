from django.urls import path
from .views import RoomListView, BookRoomView ,HomeListView,AboutView,RoomView


urlpatterns = [
    path("",HomeListView.as_view(),name='home'),
    path("about/",AboutView.as_view(),name="about"),
    path('room/', RoomView.as_view(), name='rooms'),
    path('rooms/', RoomListView.as_view(), name='room_list'),  # URL for displaying available rooms
    path('book-room/<int:room_id>/', BookRoomView.as_view(), name='book_room'),  # URL for booking a room
    # Other URL patterns as needed
]
