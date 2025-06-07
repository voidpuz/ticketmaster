from django.urls import path

from tickets.template_views import *


urlpatterns = [
    path('events/', EventListView.as_view(), name="event-list-template"),
    path('events/<int:pk>', EventDetailView.as_view(), name="event-detail-template"),
]
