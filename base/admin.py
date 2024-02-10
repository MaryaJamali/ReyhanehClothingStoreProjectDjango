from django.contrib import admin
from . import models


# Admin panel customization for the NewsletterSubscriber
@admin.register(models.NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['user', 'email', 'create_date', 'is_active']
    # Changing the fields on the Admin page
    list_editable = ['is_active']
