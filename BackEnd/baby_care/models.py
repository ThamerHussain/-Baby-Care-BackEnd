from distutils.command.upload import upload
from urllib.parse import urlsplit
from django.db import models
from restauth.models import EmailAccount 
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


# class ProductSubCategoryChoices(models.TextChoices):
#     class ClotheSubCategoryChoices(models.TextChoices):
#         BIJAMA = 'Bijama', 'BIJAMA'
#         T_SHIRT = 'T_Shirt', 'T_SHIRT'
#         UNDERWAER = 'Underwaer', 'Underwaer'

#     class FoodSubCategoryChoices(models.TextChoices):
#         MILK = 'Milk', 'MILK'
#         INSTANT_CEREAL = 'Instant_Cereal', 'INSTANT_CEREAL'

#     class FoodToolSubCategoryChoices(models.TextChoices):
#         CUP = 'Cup', 'CUP'
#         BABY_BOTTLE = 'Baby_Bottle', 'BABY_BOTTLE'

#     class ShowerToolSubCategoryChoices(models.TextChoices):
#         SOAP = 'Soap', 'SOAP'
#         TOWEL = 'Towel', 'TOWEL'
#         LOOFAH = 'Loofah', 'LOOFAH'
#         SHAMPOO = 'Shampoo', 'SHAMPOO'

#     class VehicleSubCategoryChoices(models.TextChoices):
#         JOGGER = 'Jogger', 'JOGGER'
#         STROLLER = 'Stroller', 'STROLLER'

#     class ContainerSubCategoryChoices(models.TextChoices):
#         FIXED = 'Fixed', 'FIXED'
#         MOVABLE = 'Movable', 'MOVABLE' 

#     class FurnitureSubCategoryChoices(models.TextChoices):
#         COVER = 'Cover', 'COVER'
#         PILLOW = 'Pillow', 'PILLOW'
#         MATTRESS = 'Mattress', 'MATTRESS'



class ClotheSubCategoryChoices(models.TextChoices):
    BIJAMA = 'Bijama', 'BIJAMA'
    T_SHIRT = 'T_Shirt', 'T_SHIRT'
    UNDERWAER = 'Underwaer', 'Underwaer'
    # NONE = 'None' , 'None'

class FoodSubCategoryChoices(models.TextChoices):
    MILK = 'Milk', 'MILK'
    INSTANT_CEREAL = 'Instant_Cereal', 'INSTANT_CEREAL'
    # NONE = 'None' , 'None'

class FoodToolSubCategoryChoices(models.TextChoices):
    CUP = 'Cup', 'CUP'
    BABY_BOTTLE = 'Baby_Bottle', 'BABY_BOTTLE'
    # NONE = 'None' , 'None'

class ShowerToolSubCategoryChoices(models.TextChoices):
    SOAP = 'Soap', 'SOAP'
    TOWEL = 'Towel', 'TOWEL'
    LOOFAH = 'Loofah', 'LOOFAH'
    SHAMPOO = 'Shampoo', 'SHAMPOO'
    # NONE = 'None' , 'None'

class VehicleSubCategoryChoices(models.TextChoices):
    JOGGER = 'Jogger', 'JOGGER'
    STROLLER = 'Stroller', 'STROLLER'
    # NONE = 'None' , 'None'

class ContainerSubCategoryChoices(models.TextChoices):
    FIXED = 'Fixed', 'FIXED'
    MOVABLE = 'Movable', 'MOVABLE'
    # NONE = 'None' , 'None'

class FurnitureSubCategoryChoices(models.TextChoices):
    COVER = 'Cover', 'COVER'
    PILLOW = 'Pillow', 'PILLOW'
    MATTRESS = 'Mattress', 'MATTRESS'
    # NONE = 'None' , 'None'



class AgeChoices(models.TextChoices):
    ONE_TO_SIX_MONTHS = 'One_To_Six_Months', 'ONE_TO_SIX_MONTHS'
    MORE_THAN_SIX_MONTHS = 'More_Than_Six_Months', 'MORE_THAN_SIX_MONTHS'
    # NONE = 'None' , 'None'

class ProductSexChoices(models.TextChoices):
    MALE = 'Male', 'MALE'
    FEMALE = 'Female', 'FEMALE'
    # NONE = 'None' , 'None'

class ProductSizeChoices(models.TextChoices):
    SMALL = 'Small', 'SMALL'
    MEDIUM = 'Medium', 'MEDIUM'
    LARGE = 'Large', 'LARGE'
    # NONE = 'None' , 'None'

class Product(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 255)
    price = models.CharField(max_length = 7)
    image = models.ImageField(upload_to = None)
    stars = models.CharField(max_length = 1)
    category = models.CharField(max_length = 20, choices = ProductCategoryChoices.choices)
    clothe_sub_category = models.CharField(max_length = 255, choices = ClotheSubCategoryChoices.choices, blank = True, null = True)
    food_sub_category = models.CharField(max_length = 255, choices = FoodSubCategoryChoices.choices, blank = True, null = True)
    food_tool_sub_category = models.CharField(max_length = 255, choices = FoodToolSubCategoryChoices.choices, blank = True, null = True)
    shower_tool_sub_category = models.CharField(max_length = 255, choices = ShowerToolSubCategoryChoices.choices, blank = True, null = True)
    vehicle_sub_category = models.CharField(max_length = 255, choices = VehicleSubCategoryChoices.choices, blank = True, null = True)
    container_sub_category = models.CharField(max_length = 255, choices = ContainerSubCategoryChoices.choices, blank = True, null = True)
    furniture_sub_category = models.CharField(max_length = 255, choices = FurnitureSubCategoryChoices.choices, blank = True, null = True)
    sex = models.CharField(max_length = 20, choices = ProductSexChoices.choices, blank = True, null = True)
    size = models.CharField(max_length = 20, choices = ProductSizeChoices.choices, blank = True, null = True)
    age = models.CharField(max_length = 20, choices = AgeChoices.choices, blank = True, null = True)
    # is_favourite = models.BooleanField(default = False)
    # it_bought = models.BooleanField(default = False)
    
    
    def __str__(self):
        return f'{self.name} - {self.stars}'

    @property
    def get_avg_rates(self):
        rates = self.rates.all()
        count = rates.count()
        new_list = []
        for r in rates:
            new_list.append(r.value)
        return (sum(new_list))/count

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
    def __str__(self):
        return self.full_name

class Address(models.Model):
    city = models.CharField(max_length=10 , null=True , blank=True)
    home_address = models.CharField(max_length=50 , null=True , blank=True)
    work_address = models.CharField(max_length=50 , null=True , blank=None)
    phone = models.CharField(max_length=20 , null=True , blank=True)

    def __str__(self):
        return f'{self.city} - {self.phone}'


class Item(models.Model):
    """
    Product can live alone in the system, while
    Item can only live within an order
    """
    user = models.ForeignKey(EmailAccount, verbose_name='user', related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='product', on_delete=models.CASCADE)
    item_qty = models.IntegerField('item_qty', default = 1)
    ordered = models.BooleanField('ordered')

    def __str__(self):
        return self.product.name



class OrderStatus(models.Model):
    NEW = 'NEW'  # Order with reference created, items are in the basket.
    # CREATED = 'CREATED'  # Created with items and pending payment.
    # HOLD = 'HOLD'  # Stock reduced but still awaiting payment.
    # FAILED = 'FAILED'  # Payment failed, retry is available.
    # CANCELLED = 'CANCELLED'  # Cancelled by seller, stock increased.
    PROCESSING = 'PROCESSING'  # Payment confirmed, processing order.
    SHIPPED = 'SHIPPED'  # Shipped to customer.
    COMPLETED = 'COMPLETED'  # Completed and received by customer.
    REFUNDED = 'REFUNDED'  # Fully refunded by seller.

    title = models.CharField('title', max_length=255, choices=[
        (NEW, NEW),
        (PROCESSING, PROCESSING),
        (SHIPPED, SHIPPED),
        (COMPLETED, COMPLETED),
        (REFUNDED, REFUNDED),
    ])
    is_default = models.BooleanField('is default')

    def __str__(self):
        return self.title




class Order(models.Model):
    user = models.ForeignKey(EmailAccount, verbose_name='user', related_name='orders', null=True, blank=True,
                            on_delete=models.CASCADE)
    address = models.ForeignKey(Address, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    # total = models.DecimalField('total', blank=True, null=True, max_digits=1000, decimal_places=0)
    status = models.ForeignKey(OrderStatus, verbose_name='status', related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField('note', null=True, blank=True, max_length=255)
    ref_code = models.CharField('ref code', max_length=255, null=True, blank=True)
    ordered = models.BooleanField('ordered', default=False, null=True, blank=True)
    items = models.ManyToManyField(Item, verbose_name='items', related_name='order')

    def __str__(self):
        return self.ref_code

    @property
    def order_total(self):
        order_total = sum(
            i.product.price_discounted * i.item_qty for i in self.items.all()
        )

        return order_total




class Favourite(models.Model):
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name } - {self.product.name}'




class Profile(models.Model):
    name = models.CharField(max_length = 30, null=True, blank=True)
    user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length = 15)
    city = models.CharField(max_length = 20)

    def __str__(self):
        return self.name



class Rate(models.Model):
        user = models.ForeignKey(EmailAccount, on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')
        value = models.IntegerField()
        comment = models.CharField(max_length=150)
        def __str__(self):
            return f'{self.comment} - {"BY"} - {self.user.first_name}'

