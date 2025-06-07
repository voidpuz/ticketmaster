from django.contrib import admin

from tickets.models import Event, Venue, TicketType, Seat, Ticket


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "start_time", "end_time", "is_active")
    list_filter = ("is_active",)
    search_fields = ("title", "description")
    ordering = ("start_time",)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city", "capacity", "map_urls")
    list_filter = ("city",)
    search_fields = ("name", "address")
    ordering = ("name", "address", "city", "capacity", "map_urls")


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ("seat_number", "row", "section", "venue")
    list_filter = ("venue",)
    search_fields = ("seat_number",)
    ordering = ("seat_number", "row", "section", "venue")


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "quantity", "event")
    list_filter = ("event",)
    search_fields = ("name",)
    ordering = ("name", "price", "quantity", "event")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("order", "ticket_type", "seat", "qr_code")
    list_filter = ("order", "ticket_type", "seat")
    search_fields = ("order", "ticket_type", "seat")
    ordering = ("order", "ticket_type", "seat", "qr_code")