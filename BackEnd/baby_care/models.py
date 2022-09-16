from django.db import models


class ProductCategoryChoices(models.TextChoices):
    SHOES = 'Shoe', 'SHOE'
    DIAPERS = 'Diaper', 'DIAPER'
    CLOTHES = 'Clothe', 'CLOTHE'
    VEHICLES = 'Vehicle', 'VEHICLE'
    NUTRITION = 'Nutrition', 'NUTRITION'
    EQUIPMENT = 'Equipment', 'EQUIPMENT'
    CONTAINERS = 'Container', 'CONTAINER'
    SHOWER_TOOLS = 'Shower_Tool', 'SHOWER_TOOL'
    Furniture = 'Furniture', 'FURNITURE'


# class ProductSubCategoryChoices(models.TextChoices):
class ClotheSubCategoryChoices(models.TextChoices):
        BIJAMA = 'Bijama', 'BIJAMA'
        T_SHIRT = 'T_Shirt', 'T_SHIRT'
        UNDERWAER = 'Underwaer', 'Underwaer'
        NONE = 'None', 'NONE'

class FoodSubCategoryChoices(models.TextChoices):
        MILK = 'Milk', 'MILK'
        INSTANT_CEREAL = 'Instant_Cereal', 'INSTANT_CEREAL'
        NONE = 'None', 'NONE'

class FoodToolSubCategoryChoices(models.TextChoices):
        CUP = 'Cup', 'CUP'
        BABY_BOTTLE = 'Baby_Bottle', 'BABY_BOTTLE'
        NONE = 'None', 'NONE'

class ShowerToolSubCategoryChoices(models.TextChoices):
        SOAP = 'Soap', 'SOAP'
        TOWEL = 'Towel', 'TOWEL'
        LOOFAH = 'Loofah', 'LOOFAH'
        SHAMPOO = 'Shampoo', 'SHAMPOO'
        NONE = 'None', 'NONE'

class VehicleSubCategoryChoices(models.TextChoices):
        JOGGER = 'Jogger', 'JOGGER'
        STROLLER = 'Stroller', 'STROLLER'
        NONE = 'None', 'NONE'

class ContainerSubCategoryChoices(models.TextChoices):
        FIXED = 'Fixed', 'FIXED'
        MOVABLE = 'Movable', 'MOVABLE'
        NONE = 'None', 'NONE'

class FurnitureSubCategoryChoices(models.TextChoices):
        COVER = 'Cover', 'COVER'
        PILLOW = 'Pillow', 'PILLOW'
        MATTRESS = 'Mattress', 'MATTRESS'
        NONE = 'None', 'NONE'


class AgeChoices(models.TextChoices):
    ONE_TO_SIX_MONTHS = 'One_To_Six_Months', 'ONE_TO_SIX_MONTHS'
    MORE_THAN_SIX_MONTHS = 'More_Than_Six_Months', 'MORE_THAN_SIX_MONTHS'
    NONE = 'None', 'NONE'


class ProductSexChoices(models.TextChoices):
    MALE = 'Male', 'MALE'
    FEMALE = 'Female', 'FEMALE'
    NONE = 'None', 'NONE'


class ProductSizeChoices(models.TextChoices):
    SMALL = 'Small', 'SMALL'
    MEDIUM = 'Medium', 'MEDIUM'
    LARGE = 'Large', 'LARGE'
    NONE = 'None', 'NONE'


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    price = models.CharField(max_length=7)
    image = models.ImageField(upload_to=None)
    stars = models.IntegerField()
    category = models.CharField(max_length=20, choices=ProductCategoryChoices.choices)
    # product_sub_category = models.CharField(max_length=255, choices=ProductSubCategoryChoices.choices, blank=True,
    #                                         null=True)
    ClotheSubCategoryChoices = models.CharField(max_length=255, choices=ClotheSubCategoryChoices.choices,blank=True,
                                            null=True)

    FoodSubCategoryChoices = models.CharField(max_length=255, choices=FoodSubCategoryChoices.choices,blank=True,
                                            null=True)

    FoodToolSubCategoryChoices = models.CharField(max_length=255, choices=FoodToolSubCategoryChoices.choices,blank=True,
                                            null=True)

    ShowerToolSubCategoryChoices = models.CharField(max_length=255, choices=ShowerToolSubCategoryChoices.choices,blank=True,
                                            null=True)

    VehicleSubCategoryChoices = models.CharField(max_length=255, choices=VehicleSubCategoryChoices.choices,blank=True,
                                            null=True)

    ContainerSubCategoryChoices = models.CharField(max_length=255, choices=ContainerSubCategoryChoices.choices,blank=True,
                                            null=True)

    FurnitureSubCategoryChoices = models.CharField(max_length=255, choices=FurnitureSubCategoryChoices.choices,blank=True,
                                            null=True)

    VehicleSubCategoryChoices = models.CharField(max_length=255, choices=VehicleSubCategoryChoices.choices,blank=True,
                                            null=True)

    sex = models.CharField(max_length=20, choices=ProductSexChoices.choices, blank=True, null=True)
    size = models.CharField(max_length=20, choices=ProductSizeChoices.choices, blank=True, null=True)
    age = models.CharField(max_length=20, choices=AgeChoices.choices, blank=True, null=True)
    is_favourite = models.BooleanField(default=False)
    it_bought = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - {self.stars}'



class Doctor(models.Model):
    full_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to=None)
    Specialization = models.CharField(max_length=20)
    # Working_hours = models.CharField(max_length = 20)
    cv = models.CharField(max_length=250)
    # clinic_opening_hours = models.ForeignKey(ClinicOpeningHours, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=20)
    sunday = models.CharField(default='Sunday ', max_length=20, blank=True, null=True)
    monday = models.CharField(default='Monday ', max_length=20, blank=True, null=True)
    tuesday = models.CharField(default='Tuesday ', max_length=20, blank=True, null=True)
    wednesday = models.CharField(default='Wednesday ', max_length=20, blank=True, null=True)
    thursday = models.CharField(default='Thursday ', max_length=20, blank=True, null=True)
    friday = models.CharField(default='Friday ', max_length=20, blank=True, null=True)
    saturday = models.CharField(default='Saturday ', max_length=20, blank=True, null=True)

    def __str__(self):
        return self.full_name

class Address(models.Model):
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)



