from ninja import Router
from typing import List
from baby_care.models import Product
from baby_care.schemas import Display_product
from baby_care.schemas import Display_doctor
from itertools import chain

from baby_care.models import Doctor

baby_router = Router()


# -suggestions-
@baby_router.get('/display suggestions', response=List[Display_product])
def display_suggestions(request):
    prod = Product.objects.all().filter(stars=5)
    prod2 = Product.objects.all().filter(stars=4)
    result_list = list(chain(prod, prod2))
    return result_list


# ------------------------------------
# -all product-
@baby_router.get('/display all prod', response=List[Display_product])
def display_all_prod(request):
    prod = Product.objects.all()
    return prod


# ------------------------------------


# -all doctors-
@baby_router.get('/display all doctor', response=List[Display_doctor])
def display_doctor(request):
    doctor = Doctor.objects.all()
    return doctor

#@baby_router.get('/default_clothes_without_any_choices_from_user/{filter}/', response=List[Display_product])
# ---------------filers---------------------

# -default_clothes_without_any_choices_from_user -
@baby_router.get('/default_clothes_without_any_choices_from_user', response=List[Display_product])
def default_clothes_without_any_choices_from_user(request):
    produc = Product.objects.all().filter(category="Clothe")
    return produc


# ------------------------------------

# -clothes_only_Male_and_the_size_and_category_none_from_user-
@baby_router.get('/clothes_only_Male_and_the_size_and_category_none_from_user',
                 response=List[Display_product])
def clothes_only_Male_and_the_size_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", sex='Male')
    return produc


# ------------------------------------

# -clothes_only_Female_and_the_size_and_category_none_from_user-
@baby_router.get('/clothes_only_Female_and_the_size_and_category_none_from_user',
                 response=List[Display_product])
def clothes_only_Female_and_the_size_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female")
    return produc


# ------------------------------------

# -clothes_only_Small_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Small_and_the_sex_and_category_none_from_user',
                 response=List[Display_product])
def clothes_only_Small_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Small')
    return produc


# ------------------------------------

# -clothes_only_Medium_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Medium_and_the_sex_and_category_none_from_user',
                 response=List[Display_product])
def clothes_only_Medium_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Medium')
    return produc


# ------------------------------------

# -clothes_only_Large_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Large_and_the_sex_and_category_none_from_user',
                 response=List[Display_product])
def clothes_only_Large_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Large')
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user',
                 response=List[Display_product])
def ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(ClotheSubCategoryChoices="Bijama")
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user',
                 response=List[Display_product])
def ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(ClotheSubCategoryChoices="T_Shirt")
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user',
                 response=List[Display_product])
def ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(ClotheSubCategoryChoices="Underwaer")
    return produc


# ------------------------------------

# -clothe_sex_male_size_small_category_none-
@baby_router.get('/clothe_sex_male_size_small_category_none', response=List[Display_product])
def clothe_sex_male_size_small_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small")
    return produc


# ------------------------------------

# -clothe_sex_female_size_small_category_none-
@baby_router.get('/clothe_sex_female_size_small_category_none', response=List[Display_product])
def clothe_sex_female_size_small_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small")
    return produc


# ------------------------------------

# -clothe_sex_male_size_mediuem_category_none-
@baby_router.get('/clothe_sex_male_size_mediuem_category_none', response=List[Display_product])
def clothe_sex_male_size_mediuem_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium")
    return produc


# ------------------------------------

# -clothe_sex_Female_size_mediuem_category_none-
@baby_router.get('/clothe_sex_Female_size_mediuem_category_none', response=List[Display_product])
def clothe_sex_Female_size_mediuem_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium")
    return produc


# ------------------------------------

# -clothe_sex_Male_size_Large_category_none-
@baby_router.get('/clothe_sex_Male_size_Large_category_none', response=List[Display_product])
def clothe_sex_Male_size_Large_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large")
    return produc


# ------------------------------------

# -clothe_sex_female_size_Large_category_none-
@baby_router.get('/clothe_sex_female_size_Large_category_none', response=List[Display_product])
def clothe_sex_female_size_Large_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large")
    return produc


# -clothe_sex_male_size_small_category_Bijama-
@baby_router.get('/clothe_sex_male_size_small_category_Bijama', response=List[Display_product])
def clothe_sex_male_size_small_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_male_size_small_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_small_category_T_Shirt', response=List[Display_product])
def clothe_sex_male_size_small_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_male_size_small_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_small_category_Underwaer', response=List[Display_product])
def clothe_sex_male_size_small_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# @baby_router.get('/testforloop/{filter}/',response=List[Display_product])
# def check(request):
#     user_choices = "Male"
#     if user_choices == "Male":
#         produc = Product.objects.all().filter(sex = user_choices)
#         return produc


# -clothe_sex_male_size_medium_category_Bijama-
@baby_router.get('/clothe_sex_male_size_medium_category_Bijama', response=List[Display_product])
def clothe_sex_male_size_medium_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_male_size_Large_category_Bijama-
@baby_router.get('/clothe_sex_male_size_Large_category_Bijama', response=List[Display_product])
def clothe_sex_male_size_Large_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_male_size_medium_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_medium_category_T_Shirt', response=List[Display_product])
def clothe_sex_male_size_medium_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_male_size_Large_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_Large_category_T_Shirt', response=List[Display_product])
def clothe_sex_male_size_Large_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Large", size="Medium",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_male_size_medium_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_medium_category_Underwaer', response=List[Display_product])
def clothe_sex_male_size_medium_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# -clothe_sex_male_size_Large_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_Large_category_Underwaer', response=List[Display_product])
def clothe_sex_male_size_Large_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# -clothe_sex_Female_size_Small_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_Small_category_Bijama', response=List[Display_product])
def clothe_sex_Female_size_Small_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_Female_size_medium_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_medium_category_Bijama', response=List[Display_product])
def clothe_sex_Female_size_medium_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_Female_size_Large_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_Large_category_Bijama', response=List[Display_product])
def clothe_sex_Female_size_Large_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          ClotheSubCategoryChoices="Bijama")
    return produc


# -clothe_sex_Female_size_Small_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_Small_category_tshirt', response=List[Display_product])
def clothe_sex_Female_size_Small_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_Female_size_medium_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_medium_category_tshirt', response=List[Display_product])
def clothe_sex_Female_size_medium_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_Female_size_Large_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_Large_category_tshirt', response=List[Display_product])
def clothe_sex_Female_size_Large_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          ClotheSubCategoryChoices="T_Shirt")
    return produc


# -clothe_sex_Female_size_Small_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_Small_category_Underwaer', response=List[Display_product])
def clothe_sex_Female_size_Small_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# -clothe_sex_Female_size_medium_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_medium_category_Underwaer', response=List[Display_product])
def clothe_sex_Female_size_medium_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# -clothe_sex_Female_size_Large_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_Large_category_Underwaer', response=List[Display_product])
def clothe_sex_Female_size_Large_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          ClotheSubCategoryChoices="Underwaer")
    return produc


# -diaper by default-
@baby_router.get('/diaper_by_default/{filter}/', response=List[Display_product])
def diaper_by_default(request):
    produc = Product.objects.all(category="Diaper")
    return produc


# -diaper_by_size_small-
@baby_router.get('/diaper_by_size_small', response=List[Display_product])
def diaper_by_size_small(request):
    produc = Product.objects.all().filter(category="Diaper", size="Small")
    return produc


# -diaper_by_size_medium-
@baby_router.get('/diaper_by_size_medium', response=List[Display_product])
def diaper_by_size_medium(request):
    produc = Product.objects.all().filter(category="Diaper", size="Medium")
    return produc


# -diaper_by_size_Large-
@baby_router.get('/diaper_by_size_Large', response=List[Display_product])
def diaper_by_size_Large(request):
    produc = Product.objects.all().filter(category="Diaper", size="Large")
    return produc


# -food_by_default-
@baby_router.get('/food_by_default', response=List[Display_product])
def food_by_default(request):
    produc = Product.objects.all().filter(category="Nutrition")
    return produc


# -food_by_milk_and_age_none-
@baby_router.get('/food_by_milk_and_age_none', response=List[Display_product])
def food_by_milk_and_age_none(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Milk")
    return produc


# -food_by_milk_and_age_One_To_Six_Months-
@baby_router.get('/food_by_milk_and_age_One_To_Six_Months', response=List[Display_product])
def food_by_milk_and_age_One_To_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Milk", age="One_To_Six_Months")
    return produc


# -food_by_milk_and_age_More_Than_Six_Months-
@baby_router.get('/food_by_milk_and_age_More_Than_Six_Months', response=List[Display_product])
def food_by_milk_and_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Milk",
                                          age="More_Than_Six_Months")
    return produc


# -food_by_Instant_Cereal_and_age_none-
@baby_router.get('/food_by_Instant_Cereal_and_age_none', response=List[Display_product])
def food_by_Instant_Cereal_and_age_none(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Instant_Cereal")
    return produc


# -food_by_Instant_Cereal_and_age_One_Than_Six_Months-
@baby_router.get('/food_by_milk_and_age_More_Than_Six_Months', response=List[Display_product])
def food_by_milk_and_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Instant_Cereal",
                                          age="One_To_Six_Months")
    return produc


# -food_by_Instant_Cereal_and_age_More_Than_Six_Months-
@baby_router.get('/food_by_Instant_Cereal_and_age_More_Than_Six_Months', response=List[Display_product])
def food_by_Instant_Cereal_and_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", FoodSubCategoryChoices="Instant_Cereal",
                                          age="More_Than_Six_Months")
    return produc


# -all_FoodTool-
@baby_router.get('/all_FoodTool', response=List[Display_product])
def all_FoodTool(request):
    produc = Product.objects.all(ProductCategoryChoices="Equipment")
    return produc


# -FoodTool_Cup-
@baby_router.get('/FoodTool_Cup', response=List[Display_product])
def FoodTool_Cup(request):
    produc = Product.objects.all().filter(category="Equipment", FoodToolSubCategoryChoices="Cup")
    return produc


# -FoodTool_Baby_Bottle-
@baby_router.get('/FoodTool_Baby_Bottle', response=List[Display_product])
def FoodTool_Baby_Bottle(request):
    produc = Product.objects.all().filter(category="Equipment", FoodToolSubCategoryChoices="Baby_Bottle")
    return produc


# -ShowerTool_by_default-
@baby_router.get('/ShowerTool_by_default', response=List[Display_product])
def ShowerTool_by_default(request):
    prod = Product.objects.all().filter(ShowerToolSubCategoryChoices="Soap")
    prod2 = Product.objects.all().filter(ShowerToolSubCategoryChoices="Towel")
    prod3 = Product.objects.all().filter(ShowerToolSubCategoryChoices="Loofah")
    prod4 = Product.objects.all().filter(ShowerToolSubCategoryChoices="Shampoo")

    result_list = list(chain(prod, prod2, prod3, prod4))
    return result_list


# -ShowerTool_by_soap-
@baby_router.get('/ShowerTool_by_soap', response=List[Display_product])
def ShowerTool_by_soap(request):
    prod = Product.objects.all().filter(ShowerToolSubCategoryChoices="Soap")
    return prod


# -ShowerTool_by_Towel-
@baby_router.get('/ShowerTool_by_Towel', response=List[Display_product])
def ShowerTool_by_Towel(request):
    prod = Product.objects.all().filter(ShowerToolSubCategoryChoices="Towel")
    return prod


# -ShowerTool_by_Loofah-
@baby_router.get('/ShowerTool_by_Loofah', response=List[Display_product])
def ShowerTool_by_Loofah(request):
    prod = Product.objects.all().filter(ShowerToolSubCategoryChoices="Loofah")
    return prod


# -ShowerTool_by_Shampoo-
@baby_router.get('/ShowerTool_by_Shampoo', response=List[Display_product])
def ShowerTool_by_Shampoo(request):
    prod = Product.objects.all().filter(ShowerToolSubCategoryChoices="Shampoo")
    return prod


# -all_shoe_without_user_choices
@baby_router.get('/all_shoe_without_user_choices', response=List[Display_product])
def all_shoe_without_user_choices(request):
    prod = Product.objects.all().filter(category="Shoe")
    return prod


# -all_shoe_with_sex_male_only
@baby_router.get('/all_shoe_with_sex_male_only', response=List[Display_product])
def all_shoe_with_sex_male_only(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male")
    return prod



# -all_shoe_with_sex_Female_only
@baby_router.get('/all_shoe_with_sex_Female_only', response=List[Display_product])
def all_shoe_with_sex_Female_only(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female")
    return prod



# -all_shoe_with_size_One_To_Six_Months
@baby_router.get('/all_shoe_with_size_One_To_Six_Months', response=List[Display_product])
def all_shoe_with_size_One_To_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",size="One_To_Six_Months")
    return prod


# -all_shoe_with_size_More_Than_Six_Months
@baby_router.get('/all_shoe_with_size_More_Than_Six_Months', response=List[Display_product])
def all_shoe_with_size_More_Than_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",size="More_Than_Six_Months")
    return prod



# -all_shoe_with_with_sex_female_and_One_To_Six_Months
@baby_router.get('/all_shoe_with_with_sex_female_and_One_To_Six_Months', response=List[Display_product])
def all_shoe_with_with_sex_female_and_One_To_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female",size="One_To_Six_Months")
    return prod



# -all_shoe_with_with_sex_female_and_More_Than_Six_Months
@baby_router.get('/all_shoe_with_with_sex_female_and_More_Than_Six_Months', response=List[Display_product])
def all_shoe_with_with_sex_female_and_More_Than_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female",size="More_Than_Six_Months")
    return prod



# -all_shoe_with_with_sex_Male_and_One_To_Six_Months
@baby_router.get('/all_shoe_with_with_sex_Male_and_One_To_Six_Months', response=List[Display_product])
def all_shoe_with_with_sex_Male_and_One_To_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male",size="One_To_Six_Months")
    return prod



# -all_shoe_with_with_sex_Male_and_More_Than_Six_Months
@baby_router.get('/all_shoe_with_with_sex_Male_and_More_Than_Six_Months', response=List[Display_product])
def all_shoe_with_with_sex_Male_and_More_Than_Six_Months(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male",size="More_Than_Six_Months")
    return prod



# -all_Vehicle_default
@baby_router.get('/all_Vehicle_default',response=List[Display_product])
def all_Vehicle_default(request):
    prod = Product.objects.all().filter(category="Vehicle")
    return prod



# -Vehicle_only_Jogger
@baby_router.get('/Vehicle_only_Jogger',response=List[Display_product])
def Vehicle_only_Jogger(request):
    prod = Product.objects.all().filter(category="Vehicle",VehicleSubCategoryChoices="Jogger")
    return prod



# -Vehicle_only_Stroller
@baby_router.get('/Vehicle_only_Stroller',response=List[Display_product])
def Vehicle_only_Stroller(request):
    prod = Product.objects.all().filter(category="Vehicle",VehicleSubCategoryChoices="Stroller")
    return prod



# -all_Container
@baby_router.get('/all_Container',response=List[Display_product])
def all_Container(request):
    prod = Product.objects.all().filter(category="Container")
    return prod



# -Container_with_Fixed
@baby_router.get('/Container_with_Fixed',response=List[Display_product])
def Container_with_Fixed(request):
    prod = Product.objects.all().filter(category="Container",ContainerSubCategoryChoices="Fixed")
    return prod



# -Container_with_Movable
@baby_router.get('/Container_with_Movable',response=List[Display_product])
def Container_with_Movable(request):
    prod = Product.objects.all().filter(category="Container",ContainerSubCategoryChoices="Movable")
    return prod



# -all_Furniture
@baby_router.get('/all_Furniture',response=List[Display_product])
def all_Furniture(request):
    prod = Product.objects.all().filter(category="Furniture")
    return prod



# -all_Furniture_cover
@baby_router.get('/all_Furniture_cover',response=List[Display_product])
def all_Furniture_cover(request):
    prod = Product.objects.all().filter(category="Furniture",FurnitureSubCategoryChoices="Cover")
    return prod



# -all_Furniture_Pillow
@baby_router.get('/all_Furniture_Pillow',response=List[Display_product])
def all_Furniture_Pillow(request):
    prod = Product.objects.all().filter(category="Furniture",FurnitureSubCategoryChoices="Pillow")
    return prod



# -all_Furniture_Mattress
@baby_router.get('/all_Furniture_Mattress',response=List[Display_product])
def all_Furniture_Mattress(request):
    prod = Product.objects.all().filter(category="Furniture",FurnitureSubCategoryChoices="Mattress")
    return prod


# -searching_for_product
@baby_router.get('/searching_for_product/{search_for_product}/',response=List[Display_product])
def searching_for_product(request, search_for_product:str):
    prod = Product.objects.all().filter(category= search_for_product)
    return prod



# -searching_for_doctor
@baby_router.get('/searching_for_doctor/{search_for_doctor}/',response=List[Display_doctor])
def searching_for_doctor(request, search_for_doctor:str):
    prod = Doctor.objects.all().filter(full_name= search_for_doctor)
    return prod


#3 - empty the cart and buy all item inside the cart

#add  or update item
#remove item from order
# get order
#check out the order
# create cart default = false