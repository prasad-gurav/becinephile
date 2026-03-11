import uuid

from bookings.choices import BookingStatus
from core.models import User
from django.db import models


class Booking(models.Model):
    """
    A booking model for a movie ticket.
    """

    booking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    seat_id = models.IntegerField()
    show_time = models.DateTimeField()
    booking_date = models.DateTimeField(auto_now_add=True)
    booking_status = models.CharField(max_length=20, choices=BookingStatus.choices, default=BookingStatus.PENDING)
    booking_amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.movie_id} - {self.seat_id}"


    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-booking_date"]
