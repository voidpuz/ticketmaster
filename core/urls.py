from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

urlpatterns = [
    path('users/', include('users.urls')),
    path('tickets/', include('tickets.urls')),
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path("set-language/", set_language, name="set_language"),
]