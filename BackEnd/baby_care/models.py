from distutils.command.upload import upload
from urllib.parse import urlsplit
from django.db import models

# Create your models here.

class ProductCategoryChoices(models.TextChoices):
    SHOES = 'Shoe', 'SHOE'
    DIAPERS = 'Diaper', 'DIAPER'
    CLOTHES = 'Clothe', 'CLOTHE'
    VEHICLES = 'Vehicle', 'VEHICLE'
    NUTRITION = 'Nutrition', 'NUTRITION'
    EQUIPMENT = 'Equipment', 'EQUIPMENT'
    CONTAINERS = 'Container', 'CONTAINER'
    SHOWER_TOOLS = 'Shower_Tool', 'SHOWER_TOOL'


class ProductSubCategoryChoices(models.TextChoices):
    class ClotheSubCategoryChoices:
        BIJAMA = 'Bijama', 'BIJAMA'
        T_SHIRT = 'T_Shirt', 'T_SHIRT'
        UNDERWAER = 'Underwaer', 'Underwaer'

    class FoodSubCategoryChoices:
        MILK = 'Milk', 'MILK'
        INSTANT_CEREAL = 'Instant_Cereal', 'INSTANT_CEREAL'

    class FoodToolSubCategoryChoices:
        CUP = 'Cup', 'CUP'
        BABY_BOTTLE = 'Baby_Bottle', 'BABY_BOTTLE'

    class ShowerToolSubCategoryChoices:
        SOAP = 'Soap', 'SOAP'
        TOWEL = 'Towel', 'TOWEL'
        LOOFAH = 'Loofah', 'LOOFAH'
        SHAMPOO = 'Shampoo', 'SHAMPOO'

    class VehicleSubCategoryChoices:
        JOGGER = 'Jogger', 'JOGGER'
        STROLLER = 'Stroller', 'STROLLER'

    class ContainerSubCategoryChoices:
        FIXED = 'Fixed', 'FIXED'
        MOVABLE = 'Movable', 'MOVABLE' 

    class FurnitureSubCategoryChoices:
        COVER = 'Cover', 'COVER'
        PILLOW = 'Pillow', 'PILLOW'
        MATTRESS = 'Mattress', 'MATTRESS'

class AgeChoices(models.TextChoices):
    ONE_TO_SIX_MONTHS = 'One_To_Six_Months', 'ONE_TO_SIX_MONTHS'
    MORE_THAN_SIX_MONTHS = 'More_Than_Six_Months', 'MORE_THAN_SIX_MONTHS'

class ProductSexChoices(models.TextChoices):
    MALE = 'Male', 'MALE'
    FEMALE = 'Female', 'FEMALE'

class ProductSizeChoices(models.TextChoices):
    SMALL = 'Small', 'SMALL'
    MEDIUM = 'Medium', 'MEDIUM'
    LARGE = 'Large', 'LARGE'
#this comment from omer abo resha
#this comment from omer abo resha 2
class Product(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 255)
    price = models.CharField(max_length = 7)
    image = models.ImageField(upload_to = None)
    stars = models.CharField(max_length = 1)
    category = models.CharField(max_length = 20, choices = ProductCategoryChoices.choices)
    product_sub_category = models.CharField(max_length = 255, choices = ProductSubCategoryChoices.choices, blank = True, null = True)
    sex = models.CharField(max_length = 20, choices = ProductSexChoices.choices, blank = True, null = True)
    size = models.CharField(max_length = 20, choices = ProductSizeChoices.choices, blank = True, null = True)
    age = models.CharField(max_length = 20, choices = AgeChoices.choices, blank = True, null = True)
    is_favourite = models.BooleanField(default = False)
    it_bought = models.BooleanField(default = False)

# class ClinicOpeningHours(models.Model):
#     sunday = models.CharField(default = 'Sunday', max_length=20, blank = True, null = True)
#     monday = models.CharField(default = 'Monday', max_length=20, blank = True, null = True)
#     tuesday = models.CharField(default = 'Tuesday', max_length=20, blank = True, null = True)
#     wednesday = models.CharField(default = 'Wednesday', max_length=20, blank = True, null = True)
#     thursday = models.CharField(default = 'Thursday', max_length=20, blank = True, null = True)
#     friday = models.CharField(default = 'Friday', max_length=20, blank = True, null = True)
#     saturday = models.CharField(default = 'Saturday', max_length=20, blank = True, null = True)

class Doctor(models.Model):
    full_name = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = None)
    Specialization = models.CharField(max_length = 20)
    # Working_hours = models.CharField(max_length = 20)
    cv = models.CharField(max_length = 250)
    # clinic_opening_hours = models.ForeignKey(ClinicOpeningHours, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 20)
    sunday = models.CharField(default = 'Sunday ', max_length=20, blank = True, null = True)
    monday = models.CharField(default = 'Monday ', max_length=20, blank = True, null = True)
    tuesday = models.CharField(default = 'Tuesday ', max_length=20, blank = True, null = True)
    wednesday = models.CharField(default = 'Wednesday ', max_length=20, blank = True, null = True)
    thursday = models.CharField(default = 'Thursday ', max_length=20, blank = True, null = True)
    friday = models.CharField(default = 'Friday ', max_length=20, blank = True, null = True)
    saturday = models.CharField(default = 'Saturday ', max_length=20, blank = True, null = True)

# class Address(models.Model):
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=10)

# class User(models.Model):
#     name = models.CharField(max_length=30)
#     phone = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     # password = models.CharField(max_length=255)
#     # address = models.ForeignKey(Address,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

# class Order(models.Model):
