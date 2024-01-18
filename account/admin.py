from django.contrib import admin
from . import models


# Register User's models
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'email', 'is_active']
