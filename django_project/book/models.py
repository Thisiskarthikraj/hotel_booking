
from django.db import models
from django.contrib.auth.models import User  #




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Room(models.Model):
    room_number = models.CharField(max_length=50)
    description = models.TextField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
  

    def __str__(self):
        return f"Room {self.room_number}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    room = models.ForeignKey('book.Room', on_delete=models.CASCADE)  
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} - {self.room.room_number} - {self.check_in_date} to {self.check_out_date}"
