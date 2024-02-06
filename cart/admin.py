from django.contrib import admin
from . import models


# Admin panel customization for the cart
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'payment_date', 'is_paid']


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'final_price']
