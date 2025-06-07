from django.db import models

from common.models import BaseModel


class Venue(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    city = models.ForeignKey("common.City", on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    map_urls = models.URLField(max_length=255)

    class Meta:
        verbose_name = "Venue"
        verbose_name_plural = "Venues"
    
    def __str__(self):
        return f"Venue<{self.name}>"
    

class Seat(BaseModel):
    venue = models.ForeignKey("tickets.Venue", on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    row = models.PositiveIntegerField()
    section = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Seat"
        verbose_name_plural = "Seats"

    def __str__(self):
        return f"Seat<{self.seat_number}>"
    

class Event(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    venue = models.ForeignKey("tickets.Venue", on_delete=models.CASCADE)
    organizer = models.ForeignKey("users.User", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return f"Event<{self.title}>"
    

class TicketType(BaseModel):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    event = models.ForeignKey("tickets.Event", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Ticket Type"
        verbose_name_plural = "Ticket Types"

    def __str__(self):
        return f"Ticket Type<{self.name}>"
    

class Ticket(BaseModel):
    order = models.ForeignKey("payments.Order", on_delete=models.CASCADE)
    ticket_type = models.ForeignKey("tickets.TicketType", on_delete=models.CASCADE)
    seat = models.ForeignKey("tickets.Seat", on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to="qr_codes")

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"