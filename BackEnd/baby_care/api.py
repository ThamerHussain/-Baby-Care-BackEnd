from ninja import Router
from typing import List
from baby_care.schemas import Cart_Info, display_cart, qu
from baby_care.models import Product , Order , Item , Rate , Profile as pr , Favourite
from .schemas import Display_product, Display_products, ProductId
from baby_care.schemas import Display_doctors
from baby_care.schemas import Rating_In
from baby_care.schemas import Profile
from baby_care.schemas import Fav
from baby_care.schemas import display_fav_prod
# from baby_care.schemas import fav
# from baby_care.schemas import Display_Order
from baby_care.schemas import OrderIn
from itertools import chain
from baby_care.models import Doctor
from django.http import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from restauth.authotization import AuthBearer

User = get_user_model()
baby_router = Router()

# -display product-
@baby_router.post('/display product', response = Display_product)
def display_product(request, pd : ProductId):
    product = Product.objects.get(id = pd.product_id)
    try:
        Favourite.objects.get(product_id = product.id)
        is_favorite = True
        print('success')
    except Exception as e:
        print(e)
        print('fu*k')
        is_favorite = False
    # values = getattr(product, ['name', 'price', 'image', 'description'])
    # result = {'name': values[0], 'price': values[1], 'image': values[2], 'stars': values[3], 'description': values[4], 'is_favorite': is_favorite}
    result = {'name': product.name, 'price': product.price, 'image': f'{product.image}', 'stars': product.stars, 'description': product.description, 'is_favorite': is_favorite}
    
    # name: str
    # price: str
    # image: str
    # stars: int
    # description: str
    # is_favorite: bool
    
    return result
    # try:
    #     favo = Favourite.objects.get(product_id = id)
    #     print(favo)
    #     print('success')
    # except Exception as e:
    #     print(e)
    #     print('fu*k')
    # return 1

# -suggestions-
@baby_router.get('/display suggestions', response=List[Display_products])
def display_suggestions(request):
    prod = Product.objects.all().filter(stars=5)
    prod2 = Product.objects.all().filter(stars=4)
    result_list = list(chain(prod, prod2))
    return result_list



# ------------------------------------
# -all product-
@baby_router.get('/display all prod', response=List[Display_products])
def display_all_prod(request):
    prod = Product.objects.all()
    return prod


# ------------------------------------


# -all doctors-
@baby_router.get('/display all doctor', response=List[Display_doctors])
def display_doctor(request):
    doctor = Doctor.objects.all()
    return doctor


# -doctors from Baghdad-
@baby_router.get('/doctors from Baghdad', response=List[Display_doctors])
def display_doctor_from_Baghdad(request):
    doctor = Doctor.objects.all().filter(location = 'Baghdad')
    return doctor


# -doctors from Basrah-
@baby_router.get('/doctors from Basrah', response=List[Display_doctors])
def display_doctor_from_Basrah(request):
    doctor = Doctor.objects.all().filter(location = 'Basrah')
    return doctor


# -doctors from Mosul-
@baby_router.get('/doctors from Mosul', response=List[Display_doctors])
def display_doctor_from_Mosul(request):
    doctor = Doctor.objects.all().filter(location = 'Mosul')
    return doctor


# -doctors from Other-
@baby_router.get('/doctors from Other', response=List[Display_doctors])
def display_doctor_from_Other(request):
    doctor = Doctor.objects.all().filter(location = 'Other')
    return doctor


# -doctors with sex Male-
@baby_router.get('/doctors with sex Male', response=List[Display_doctors])
def display_doctor_with_sex_Male(request):
    doctor = Doctor.objects.all().filter(sex = 'Male')
    return doctor


# -doctors with sex Female-
@baby_router.get('/doctors with sex Female', response=List[Display_doctors])
def display_doctor_with_sex_Female(request):
    doctor = Doctor.objects.all().filter(sex = 'Female')
    return doctor


# -doctors that Available-
@baby_router.get('/doctors that Available', response=List[Display_doctors])
def display_doctor_that_Available(request):
    doctor = Doctor.objects.all().filter(availability = 'Available')
    return doctor


# -doctors that NotAvailable-
@baby_router.get('/doctors that NotAvailable', response=List[Display_doctors])
def display_doctor_that_NotAvailable(request):
    doctor = Doctor.objects.all().filter(availability = 'NotAvailable')
    return doctor




#@baby_router.get('/default_clothes_without_any_choices_from_user/{filter}/', response=List[Display_products])
# ---------------filers---------------------

# -default_clothes_without_any_choices_from_user -
@baby_router.get('/default_clothes_without_any_choices_from_user', response=List[Display_products])
def default_clothes_without_any_choices_from_user(request):
    produc = Product.objects.all().filter(category="Clothe")
    return produc


# ------------------------------------

# -clothes_only_Male_and_the_size_and_category_none_from_user-
@baby_router.get('/clothes_only_Male_and_the_size_and_category_none_from_user',
                 response=List[Display_products])
def clothes_only_Male_and_the_size_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", sex='Male')
    return produc


# ------------------------------------

# -clothes_only_Female_and_the_size_and_category_none_from_user-
@baby_router.get('/clothes_only_Female_and_the_size_and_category_none_from_user',
                 response=List[Display_products])
def clothes_only_Female_and_the_size_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female")
    return produc


# ------------------------------------

# -clothes_only_Small_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Small_and_the_sex_and_category_none_from_user',
                 response=List[Display_products])
def clothes_only_Small_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Small')
    return produc


# ------------------------------------

# -clothes_only_Medium_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Medium_and_the_sex_and_category_none_from_user',
                 response=List[Display_products])
def clothes_only_Medium_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Medium')
    return produc


# ------------------------------------

# -clothes_only_Large_and_the_sex_and_category_none_from_user-
@baby_router.get('/clothes_only_Large_and_the_sex_and_category_none_from_user',
                 response=List[Display_products])
def clothes_only_Large_and_the_sex_and_category_none_from_user(request):
    produc = Product.objects.all().filter(category="Clothe", size='Large')
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user',
                 response=List[Display_products])
def ClotheSubCategory_only_Bijama_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(clothe_sub_category="Bijama")
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user',
                 response=List[Display_products])
def ClotheSubCategory_only_Tshirt_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(clothe_sub_category="T_Shirt")
    return produc


# ------------------------------------

# -ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user-
@baby_router.get('/ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user',
                 response=List[Display_products])
def ClotheSubCategory_only_Underwaer_and_the_sex_and_size_none_from_user(request):
    produc = Product.objects.all().filter(clothe_sub_category="Underwaer")
    return produc


# ------------------------------------

# -clothe_sex_male_size_small_category_none-
@baby_router.get('/clothe_sex_male_size_small_category_none', response=List[Display_products])
def clothe_sex_male_size_small_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small")
    return produc


# ------------------------------------

# -clothe_sex_female_size_small_category_none-
@baby_router.get('/clothe_sex_female_size_small_category_none', response=List[Display_products])
def clothe_sex_female_size_small_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small")
    return produc


# ------------------------------------

# -clothe_sex_male_size_mediuem_category_none-
@baby_router.get('/clothe_sex_male_size_mediuem_category_none', response=List[Display_products])
def clothe_sex_male_size_mediuem_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",clothe_sub_category="T_Shirt")
    return produc


# ------------------------------------

# -clothe_sex_Female_size_mediuem_category_none-
@baby_router.get('/clothe_sex_Female_size_mediuem_category_none', response=List[Display_products])
def clothe_sex_Female_size_mediuem_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium")
    return produc


# ------------------------------------

# -clothe_sex_Male_size_Large_category_none-
@baby_router.get('/clothe_sex_Male_size_Large_category_none', response=List[Display_products])
def clothe_sex_Male_size_Large_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large")
    return produc


# ------------------------------------

# -clothe_sex_female_size_Large_category_none-
@baby_router.get('/clothe_sex_female_size_Large_category_none', response=List[Display_products])
def clothe_sex_female_size_Large_category_none(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large")
    return produc


# -clothe_sex_male_size_small_category_Bijama-
@baby_router.get('/clothe_sex_male_size_small_category_Bijama', response=List[Display_products])
def clothe_sex_male_size_small_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_male_size_small_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_small_category_T_Shirt', response=List[Display_products])
def clothe_sex_male_size_small_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          clothe_sub_category="T_Shirt")
    return produc


# -clothe_sex_male_size_small_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_small_category_Underwaer', response=List[Display_products])
def clothe_sex_male_size_small_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Small",
                                          clothe_sub_category="Underwaer")
    return produc


# @baby_router.get('/testforloop/{filter}/',response=List[Display_products])
# def check(request):
#     user_choices = "Male"
#     if user_choices == "Male":
#         produc = Product.objects.all().filter(sex = user_choices)
#         return produc


# -clothe_sex_male_size_medium_category_Bijama-
@baby_router.get('/clothe_sex_male_size_medium_category_Bijama', response=List[Display_products])
def clothe_sex_male_size_medium_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_male_size_Large_category_Bijama-
@baby_router.get('/clothe_sex_male_size_Large_category_Bijama', response=List[Display_products])
def clothe_sex_male_size_Large_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_male_size_medium_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_medium_category_T_Shirt', response=List[Display_products])
def clothe_sex_male_size_medium_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          clothe_sub_category="T_Shirt")
    return produc


# -clothe_sex_male_size_Large_category_T_Shirt-
@baby_router.get('/clothe_sex_male_size_Large_category_T_Shirt', response=List[Display_products])
def clothe_sex_male_size_Large_category_T_Shirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Large", size="Medium",
                                          clothe_sub_category="T_Shirt")
    return produc


# -clothe_sex_male_size_medium_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_medium_category_Underwaer', response=List[Display_products])
def clothe_sex_male_size_medium_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium",
                                          clothe_sub_category="Underwaer")
    return produc


# -clothe_sex_male_size_Large_category_Underwaer-
@baby_router.get('/clothe_sex_male_size_Large_category_Underwaer', response=List[Display_products])
def clothe_sex_male_size_Large_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Large",
                                          clothe_sub_category="Underwaer")
    return produc


# -clothe_sex_Female_size_Small_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_Small_category_Bijama', response=List[Display_products])
def clothe_sex_Female_size_Small_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_Female_size_medium_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_medium_category_Bijama', response=List[Display_products])
def clothe_sex_Female_size_medium_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_Female_size_Large_category_Bijama-
@baby_router.get('/clothe_sex_Female_size_Large_category_Bijama', response=List[Display_products])
def clothe_sex_Female_size_Large_category_Bijama(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          clothe_sub_category="Bijama")
    return produc


# -clothe_sex_Female_size_Small_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_Small_category_tshirt', response=List[Display_products])
def clothe_sex_Female_size_Small_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small",
                                          clothe_sub_category="T_Shirt")
    return produc





# # -clothe_sex_male_size_mediuem_category_none-
# @baby_router.get('/clothe_sex_male_size_mediuem_category_none', response=List[Display_products])
# def clothe_sex_male_size_mediuem_category_none(request):
#     produc = Product.objects.all().filter(category="Clothe", sex="Male", size="Medium")
#     return produc



















# -clothe_sex_Female_size_medium_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_medium_category_tshirt', response=List[Display_products])
def clothe_sex_Female_size_medium_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          clothe_sub_category="T_Shirt")
    return produc


# -clothe_sex_Female_size_Large_category_tshirt-
@baby_router.get('/clothe_sex_Female_size_Large_category_tshirt', response=List[Display_products])
def clothe_sex_Female_size_Large_category_tshirt(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          clothe_sub_category="T_Shirt")
    return produc


# -clothe_sex_Female_size_Small_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_Small_category_Underwaer', response=List[Display_products])
def clothe_sex_Female_size_Small_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Small",
                                          clothe_sub_category="Underwaer")
    return produc


# -clothe_sex_Female_size_medium_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_medium_category_Underwaer', response=List[Display_products])
def clothe_sex_Female_size_medium_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Medium",
                                          clothe_sub_category="Underwaer")
    return produc


# -clothe_sex_Female_size_Large_category_Underwaer-
@baby_router.get('/clothe_sex_Female_size_Large_category_Underwaer', response=List[Display_products])
def clothe_sex_Female_size_Large_category_Underwaer(request):
    produc = Product.objects.all().filter(category="Clothe", sex="Female", size="Large",
                                          clothe_sub_category="Underwaer")
    return produc


# -diaper by default-
@baby_router.get('/diaper_by_default', response = List[Display_products])
def diaper_by_default(request):
    produc = Product.objects.all().filter(category="Diaper")
    return produc


# -diaper_by_size_small-
@baby_router.get('/diaper_by_size_small', response=List[Display_products])
def diaper_by_size_small(request):
    produc = Product.objects.all().filter(category="Diaper", size="Small")
    return produc


# -diaper_by_size_medium-
@baby_router.get('/diaper_by_size_medium', response=List[Display_products])
def diaper_by_size_medium(request):
    produc = Product.objects.all().filter(category="Diaper", size="Medium")
    return produc


# -diaper_by_size_Large-
@baby_router.get('/diaper_by_size_Large', response=List[Display_products])
def diaper_by_size_Large(request):
    produc = Product.objects.all().filter(category="Diaper", size="Large")
    return produc





# -food_by_default-
@baby_router.get('/food_by_default', response=List[Display_products])
def food_by_default(request):
    produc = Product.objects.all().filter(category="Nutrition")
    return produc

# -food_by_age_One_To_Six_Months-
@baby_router.get('/food_by_age_One_To_Six_Months', response=List[Display_products])
def food_by_age_One_To_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", age="One_To_Six_Months")
    return produc


# -food_by_age_More_Than_Six_Months-
@baby_router.get('/food_by_age_More_Than_Six_Months', response=List[Display_products])
def food_by_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", age="More_Than_Six_Months")
    return produc



# -food_by_milk_and_age_none-
@baby_router.get('/food_by_milk_and_age_none', response=List[Display_products])
def food_by_milk_and_age_none(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Milk")
    return produc



# -food_by_milk_and_age_One_To_Six_Months-
@baby_router.get('/food_by_milk_and_age_One_To_Six_Months', response=List[Display_products])
def food_by_milk_and_age_One_To_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Milk", age="One_To_Six_Months")
    return produc


# -food_by_milk_and_age_More_Than_Six_Months-
@baby_router.get('/food_by_milk_and_age_More_Than_Six_Months', response=List[Display_products])
def food_by_milk_and_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Milk",
                                        age="More_Than_Six_Months")
    return produc


# -food_by_Instant_Cereal_and_age_none-
@baby_router.get('/food_by_Instant_Cereal_and_age_none', response=List[Display_products])
def food_by_Instant_Cereal_and_age_none(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Instant_Cereal")
    return produc


# -food_by_Instant_Cereal_and_age_One_Than_Six_Months-
@baby_router.get('/food_by_Instant_Cereal_and_age_One_To_Six_Months', response=List[Display_products])
def food_by_Instant_Cereal_and_age_One_To_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Instant_Cereal", age="One_To_Six_Months")
    return produc


# -food_by_Instant_Cereal_and_age_More_Than_Six_Months-
@baby_router.get('/food_by_Instant_Cereal_and_age_More_Than_Six_Months', response=List[Display_products])
def food_by_Instant_Cereal_and_age_More_Than_Six_Months(request):
    produc = Product.objects.all().filter(category="Nutrition", food_sub_category="Instant_Cereal",
                                          age="More_Than_Six_Months")
    return produc






# -all_FoodTool-
@baby_router.get('/all_FoodTool', response=List[Display_products])
def all_FoodTool(request):
    produc = Product.objects.all().filter(category="Equipment")
    return produc


# -FoodTool_Cup-
@baby_router.get('/FoodTool_Cup', response=List[Display_products])
def FoodTool_Cup(request):
    produc = Product.objects.all().filter(category="Equipment", food_tool_sub_category="Cup")
    return produc


# -FoodTool_Baby_Bottle-
@baby_router.get('/FoodTool_Baby_Bottle', response=List[Display_products])
def FoodTool_Baby_Bottle(request):
    produc = Product.objects.all().filter(category="Equipment", food_tool_sub_category="Baby_Bottle")
    return produc


# -ShowerTool_by_default-
@baby_router.get('/ShowerTool_by_default', response=List[Display_products])
def ShowerTool_by_default(request):
    prod = Product.objects.all().filter(shower_tool_sub_category="Soap")
    prod2 = Product.objects.all().filter(shower_tool_sub_category="Towel")
    prod3 = Product.objects.all().filter(shower_tool_sub_category="Loofah")
    prod4 = Product.objects.all().filter(shower_tool_sub_category="Shampoo")

    result_list = list(chain(prod, prod2, prod3, prod4))
    return result_list


# -ShowerTool_by_soap-
@baby_router.get('/ShowerTool_by_soap', response=List[Display_products])
def ShowerTool_by_soap(request):
    prod = Product.objects.all().filter(shower_tool_sub_category="Soap")
    return prod


# -ShowerTool_by_Towel-
@baby_router.get('/ShowerTool_by_Towel', response=List[Display_products])
def ShowerTool_by_Towel(request):
    prod = Product.objects.all().filter(shower_tool_sub_category="Towel")
    return prod


# -ShowerTool_by_Loofah-
@baby_router.get('/ShowerTool_by_Loofah', response=List[Display_products])
def ShowerTool_by_Loofah(request):
    prod = Product.objects.all().filter(shower_tool_sub_category="Loofah")
    return prod


# -ShowerTool_by_Shampoo-
@baby_router.get('/ShowerTool_by_Shampoo', response=List[Display_products])
def ShowerTool_by_Shampoo(request):
    prod = Product.objects.all().filter(shower_tool_sub_category="Shampoo")
    return prod


# -all_shoe_without_user_choices
@baby_router.get('/all_shoe_without_user_choices', response=List[Display_products])
def all_shoe_without_user_choices(request):
    prod = Product.objects.all().filter(category="Shoe")
    return prod


# -all_shoe_with_sex_male_only
@baby_router.get('/all_shoe_with_sex_male_only', response=List[Display_products])
def all_shoe_with_sex_male_only(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male")
    return prod



# -all_shoe_with_sex_Female_only
@baby_router.get('/all_shoe_with_sex_Female_only', response=List[Display_products])
def all_shoe_with_sex_Female_only(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female")
    return prod


# # -diaper_by_size_small-
# @baby_router.get('/diaper_by_size_small', response=List[Display_products])
# def diaper_by_size_small(request):
#     produc = Product.objects.all().filter(category="Diaper", size="Small")
#     return produc


# # -diaper_by_size_medium-
# @baby_router.get('/diaper_by_size_medium', response=List[Display_products])
# def diaper_by_size_medium(request):
#     produc = Product.objects.all().filter(category="Diaper", size="Medium")
#     return produc


# # -diaper_by_size_Large-
# @baby_router.get('/diaper_by_size_Large', response=List[Display_products])
# def diaper_by_size_Large(request):
#     produc = Product.objects.all().filter(category="Diaper", size="Large")
#     return produc




# -all_shoe_with_size_small
@baby_router.get('/all_shoe_with_size_Small', response=List[Display_products])
def all_shoe_with_size_Small(request):
    prod = Product.objects.all().filter(category="Shoe",size="Small")
    return prod


# -all_shoe_with_size_Medium
@baby_router.get('/all_shoe_with_size_Medium', response=List[Display_products])
def all_shoe_with_size_Medium(request):
    prod = Product.objects.all().filter(category="Shoe",size="Medium")
    return prod


# -all_shoe_with_size_Large
@baby_router.get('/all_shoe_with_size_Large', response=List[Display_products])
def all_shoe_with_size_Large(request):
    prod = Product.objects.all().filter(category="Shoe",size="Large")
    return prod





# -all_shoe_with_with_sex_female_and_Size_Small
@baby_router.get('/all_shoe_with_with_sex_female_and_Size_Small', response=List[Display_products])
def all_shoe_with_with_sex_female_and_Size_Small(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female",size="Small")
    return prod



# -all_shoe_with_with_sex_female_and_Size_Medium
@baby_router.get('/all_shoe_with_with_sex_female_and_Size_Medium', response=List[Display_products])
def all_shoe_with_with_sex_female_and_Size_Medium(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female",size="Medium")
    return prod



# -all_shoe_with_with_sex_female_and_Size_Large
@baby_router.get('/all_shoe_with_with_sex_female_and_Size_Large', response=List[Display_products])
def all_shoe_with_with_sex_female_and_Size_Large(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Female",size="Large")
    return prod



# -all_shoe_with_with_sex_Male_and_Size_Small
@baby_router.get('/all_shoe_with_with_sex_Male_and_Size_Small', response=List[Display_products])
def all_shoe_with_with_sex_Male_and_Size_Small(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male",size="Small")
    return prod



# -all_shoe_with_with_sex_Male_and_Size_Medium
@baby_router.get('/all_shoe_with_with_sex_Male_and_Size_Medium', response=List[Display_products])
def all_shoe_with_with_sex_Male_and_Size_Medium(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male",size="Medium")
    return prod



# -all_shoe_with_with_sex_Male_and_Size_Large
@baby_router.get('/all_shoe_with_with_sex_Male_and_Size_Large', response=List[Display_products])
def all_shoe_with_with_sex_Male_and_Size_Large(request):
    prod = Product.objects.all().filter(category="Shoe",sex="Male",size="Large")
    return prod






# -all_Vehicle_default
@baby_router.get('/all_Vehicle_default',response=List[Display_products])
def all_Vehicle_default(request):
    prod = Product.objects.all().filter(category="Vehicle")
    return prod



# -Vehicle_only_Jogger
@baby_router.get('/Vehicle_only_Jogger',response=List[Display_products])
def Vehicle_only_Jogger(request):
    prod = Product.objects.all().filter(category="Vehicle",vehicle_sub_category="Jogger")
    return prod



# -Vehicle_only_Stroller
@baby_router.get('/Vehicle_only_Stroller',response=List[Display_products])
def Vehicle_only_Stroller(request):
    prod = Product.objects.all().filter(category="Vehicle",vehicle_sub_category="Stroller")
    return prod



# -all_Container
@baby_router.get('/all_Container',response=List[Display_products])
def all_Container(request):
    prod = Product.objects.all().filter(category="Container")
    return prod



# -Container_with_Fixed
@baby_router.get('/Container_with_Fixed',response=List[Display_products])
def Container_with_Fixed(request):
    prod = Product.objects.all().filter(category="Container",container_sub_category="Fixed")
    return prod



# -Container_with_Movable
@baby_router.get('/Container_with_Movable',response=List[Display_products])
def Container_with_Movable(request):
    prod = Product.objects.all().filter(category="Container",container_sub_category="Movable")
    return prod



# -all_Furniture
@baby_router.get('/all_Furniture',response=List[Display_products])
def all_Furniture(request):
    prod = Product.objects.all().filter(category="Furniture")
    return prod



# -all_Furniture_cover
@baby_router.get('/all_Furniture_cover',response=List[Display_products])
def all_Furniture_cover(request):
    prod = Product.objects.all().filter(category="Furniture",furniture_sub_category="Cover")
    return prod



# -all_Furniture_Pillow
@baby_router.get('/all_Furniture_Pillow',response=List[Display_products])
def all_Furniture_Pillow(request):
    prod = Product.objects.all().filter(category="Furniture",furniture_sub_category="Pillow")
    return prod



# -all_Furniture_Mattress
@baby_router.get('/all_Furniture_Mattress',response=List[Display_products])
def all_Furniture_Mattress(request):
    prod = Product.objects.all().filter(category="Furniture",furniture_sub_category="Mattress")
    return prod


# -searching_for_product
@baby_router.get('/searching_for_product/{search_for_product}/',response=List[Display_products])
def searching_for_product(request, search_for_product:str):
    try:
        prod = Product.objects.all().filter(category= search_for_product)
        return prod
    finally:
        if not prod:
            raise Http404(f'this {search_for_product} doesnt exist')




# -searching_for_doctor
@baby_router.get('/searching_for_doctor/{search_for_doctor}/',response =List[Display_doctors])
def searching_for_doctor(request, search_for_doctor:str):
    try:
        prod = Doctor.objects.all().filter(full_name= search_for_doctor)
        return prod
    finally:
        if not prod:
            raise Http404(f'this {search_for_doctor} doesnt exist')



# @baby_router.get('/get_all_order', response=List[Display_Order])
# def get_order(request):
#     order = Order.objects.all()
#     return order



#3 - empty the cart and buy all item inside the cart

#add  or update item
#remove item from order
# get order
#check out the order
# create cart default = false






@baby_router.post("/Order" , response=OrderIn, auth= AuthBearer())
def create_order(request, payload: OrderIn):
    user = get_object_or_404(User, email= request.auth['email'])
    try:
        order = Order.objects.get(ordered=False, user=user)

        # order.items.add()
    except Order.DoesNotExist:
        order = Order.objects.create(
                user=user,
                status_id=payload.status_id,
                note=payload.note,
                ref_code= payload.ref_code,
                ordered=False,
                address_id=payload.address_id
                )

        items = Item.objects.filter(id__in=payload.items_id)
        order.items.add(*items)
        items.update(ordered=True)
        items.save()
        order.save()

    return order

# user = get_object_or_404(User, email= request.auth['email'])
# order = Order.objects.get(ordered=False, user=user)
# item = Item.objects.filter(id=item_id)
# order.items.add(*item)
# item.update(ordered=True)
# item.save()
# order.save()



@baby_router.post("/rating" , response=Rating_In, auth= AuthBearer())
def create_rating(request , payload:Rating_In):
    user = get_object_or_404(User, email= request.auth['email'])

    rating = Rate.objects.create(
                user=user,
                product_id = payload.product_id,
                value = payload.value,
                comment = payload.comment
                
                )
    rating.save()
    return rating



# @baby_router.get('/display all profile', response=List[Profile])
# def display_all_profile(request):
#     prof = pr.objects.all()
#     return prof




@baby_router.get('/display_current_profile', response=List[Profile] , auth= AuthBearer())
def display_current_profile(request):
    user = get_object_or_404(User, email= request.auth['email'])
    pro = pr.objects.filter(user = user)
    return pro





@baby_router.post("/Create_Favourite" ,  auth= AuthBearer())
def Create_Favourite(request , payload:Fav):
    user = get_object_or_404(User, email= request.auth['email'])
    
    try:
        product = Product.objects.get(name = payload.name)
        fa = Favourite.objects.get_or_create(
                    user=user,
                    product_id = product.id,
                    )
        # fa.save()
        print("Record saved successfully!")
        
    
    except:
        print("Record doesn't exists")
    return 1
    

@baby_router.post("/Remove_Favourite", auth= AuthBearer())
def Remove_Favourite(request , payload:Fav):
    user = get_object_or_404(User, email= request.auth['email'])

    try:
        product = Product.objects.get(name = payload.name)
        fa = Favourite.objects.get(
                    user=user,
                    product_id = product.id,
                    )
        fa.delete()
        print("Record deleted successfully!")


    except:
        print("Record doesn't exists")
    return 1


@baby_router.get('/get_the_fav_prod_from_the_current_user', response=List[display_fav_prod] , auth= AuthBearer())
def get_the_fav_prod_from_the_current_user(request):
    user = get_object_or_404(User, email= request.auth['email'])
    fav = Favourite.objects.filter(user = user)
    return fav




@baby_router.post("/Add_item_to_cart", auth= AuthBearer())
def Add_item_to_cart(request , payload:Cart_Info):
    user = get_object_or_404(User, email= request.auth['email'])
    
    product = Product.objects.get(name = payload.name)
    
    item = Item.objects.get_or_create(
                user=user,
                product_id = product.id,
                )
    # item.save()
    return 1





@baby_router.get('/get_the_cart_from_the_current_user', response=List[display_cart] , auth= AuthBearer())
def get_the_cart_from_the_current_user(request):
    user = get_object_or_404(User, email= request.auth['email'])
    item = Item.objects.filter(user = user)
    return item



@baby_router.put("/change_qu_+", auth= AuthBearer())
def change_quplu(request , payload: qu):
    user = get_object_or_404(User, email= request.auth['email'])
    product = Product.objects.get(name = payload.name)
    item = Item.objects.get(product_id = product.id, user = user)
    item.item_qty=item.item_qty +1
    item.save()
    return 1



@baby_router.put("/change_qu_-" , auth= AuthBearer())
def change_qu_min(request , payload: qu):
    user = get_object_or_404(User, email= request.auth['email'])
    product = Product.objects.get(name = payload.name)
    item = Item.objects.get(product_id = product.id, user = user)
    if item.item_qty == 1: 
        item.delete() 
        return 1  
    item.item_qty += 1
    item.save()
    return 1