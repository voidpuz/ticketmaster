from django.contrib import admin

from common.models import City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "soato")