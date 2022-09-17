from django.contrib import admin

from .models import Product, Doctor#, ClinicOpeningHours

# Register your models here.
class Config(admin.ModelAdmin):
    # admin.site.register(ClinicOpeningHours)
    admin.site.register(Product)
    admin.site.register(Doctor)