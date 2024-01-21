from django.contrib import admin
from . import models


# Admin panel customization for the SiteSetting
@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['site_name', 'site_url', 'phone', 'email', 'is_main_setting']


# Admin panel customization for the Slider
@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'display_order']
    # Changing the fields on the Admin page
    list_editable = ['display_order']


# Admin panel customization for the FooterLinkBox
admin.site.register(models.FooterLinkBox)


# Admin panel customization for the FooterLink
@admin.register(models.FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']
