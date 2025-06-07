from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email", "phone_number", "first_name", "last_name", "is_organizer", "is_active")
    search_fields = ("email", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'phone_number', 'avatar', 'bio')}),
        (('Permissions'), {
            'fields': ('is_active', 'is_confirmed', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }), 
    )

    ordering = ('email',)