from django.contrib import admin

from payments.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("user", "total_amount", "is_paid")
    list_filter = ("is_paid",)