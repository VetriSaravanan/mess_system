from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the admin list view
    list_display = ('username', 'email', 'role', 'is_active', 'is_staff')

    # Fields to filter by in the admin list view
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')

    # Fields to show in the admin form for user editing
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number')}),
    )

    # Fields to include when creating a new user in the admin
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone_number')}),
    )

    # Search functionality in admin
    search_fields = ('username', 'email', 'role')

# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)
