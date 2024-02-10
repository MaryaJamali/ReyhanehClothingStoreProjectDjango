from django.contrib import admin
from . import models


# Admin panel customization for the NewsletterSubscription
@admin.register(models.NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['user', 'email', 'create_date', 'is_active']
    # Changing the fields on the Admin page
    list_editable = ['is_active']
