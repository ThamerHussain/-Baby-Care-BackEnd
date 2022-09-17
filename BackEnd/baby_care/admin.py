from django.contrib import admin

from .models import Product, Doctor, Item, Order, OrderStatus#, ClinicOpeningHours

# Register your models here.
class Config(admin.ModelAdmin):
    # admin.site.register(ClinicOpeningHours)
    admin.site.register(Product)
    admin.site.register(Doctor)
    admin.site.register(Item)
    admin.site.register(Order)
    admin.site.register(OrderStatus)