from django.contrib import admin

from .models import Product, Doctor, Item, Order, OrderStatus, Address , Favourite  , Profile , Rate , Card

# Register your models here.
class Config(admin.ModelAdmin):
    admin.site.register(Product)
    admin.site.register(Doctor)
    admin.site.register(Item)
    admin.site.register(Order)
    admin.site.register(OrderStatus)
    admin.site.register(Address)
    admin.site.register(Favourite)
    # admin.site.register(Comment)
    admin.site.register(Profile)
    admin.site.register(Rate)
    admin.site.register(Card)