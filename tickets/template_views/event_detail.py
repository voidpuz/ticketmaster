from django.views.generic import DetailView

from tickets.models import Event


class EventDetailView(DetailView):
    queryset = Event.objects.filter(is_active=True)
    template_name = "events/event_detail.html"
    context_object_name = "event"