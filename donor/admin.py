from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, DonorProfile

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address', 'latitude', 'longitude')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address', 'latitude', 'longitude')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff')

admin.site.register(User, CustomUserAdmin)
admin.site.register(DonorProfile)
