from django.views.generic import (
    ListView, 
)

from tickets.models import Event


class EventListView(ListView):
    queryset = Event.objects.filter(is_active=True).order_by('start_time')
    template_name = "events/events_list.html"
    context_object_name = "events_list"