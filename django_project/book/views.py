from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView,View
from .models import Room , Booking
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class RoomListView(ListView):
    model=Room
    template_name="room.html"
   
class RoomView(ListView):
    model=Room
    template_name="roomlist.html" 
class HomeListView(ListView):
    model=Room
    template_name="home.html"

class AboutView(ListView):
    model=Room
    template_name="about.html"

class BookRoomView(View):
    def get(self, request, room_id):
        selected_room = get_object_or_404(Room, pk=room_id)
        return render(request, 'booking_form.html', {'room': selected_room})

    def post(self, request, room_id):
        selected_room = get_object_or_404(Room, pk=room_id)
        user = request.user  # Assuming the user is authenticated
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        new_booking = Booking.objects.create(
            user=user,
            room=selected_room,
            check_in_date=check_in_date,
            check_out_date=check_out_date
        )
        selected_room.availability = False
        selected_room.save()
        return render(request, 'booking_confirmation.html')
    def delete(self,room_id):
        selected_room = get_object_or_404(Room,pk=room_id)
        room=selected_room,
        selected_room.availability=True
        self.room.save()
