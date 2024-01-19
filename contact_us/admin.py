from django.contrib import admin
from . import models


# Admin panel customization for the ContactUs
@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['full_name', 'email', 'phone_number', 'created_date', 'is_read_by_admin']
    # Changing the fields on the Admin page
    list_editable = ['is_read_by_admin']
