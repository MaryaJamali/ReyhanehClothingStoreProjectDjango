from django.contrib import admin
from . import models


# Admin panel customization for the SiteSetting
@admin.register(models.SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    # Display fields on the Admin page
    list_display = ['site_name', 'site_url', 'phone', 'email', 'is_main_setting']


# Admin panel customization for the MenuLinkBox
admin.site.register(models.MenuLinkBox)


# Admin panel customization for the MenuLink
@admin.register(models.MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# Admin panel customization for the Slider
@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'display_order', 'is_active']
    # Changing the fields on the Admin page
    list_editable = ['display_order', 'is_active']


# Admin panel customization for the FooterLinkBox
admin.site.register(models.FooterLinkBox)


# Admin panel customization for the FooterLink
@admin.register(models.FooterLink)
class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']


# Admin panel customization for the QuestionCommonGroup
admin.site.register(models.QuestionCommonGroup)


# Admin panel customization for the QuestionCommon
@admin.register(models.QuestionCommon)
class QuestionCommonAdmin(admin.ModelAdmin):
    list_display = ['question_common_group', 'question', 'response']
