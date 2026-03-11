from django.db.models import TextChoices


class BookingStatus(TextChoices):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
