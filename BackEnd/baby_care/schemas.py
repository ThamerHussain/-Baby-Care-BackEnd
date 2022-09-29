from ninja import Schema


# all product
class Display_product(Schema):
    name: str
    description: str
    price: str
    image: str
    stars: int
    category: str
    ClotheSubCategoryChoices: str = None
    FoodSubCategoryChoices: str = None
    FoodToolSubCategoryChoices: str = None
    ShowerToolSubCategoryChoices: str = None
    VehicleSubCategoryChoices: str = None
    ContainerSubCategoryChoices: str = None
    FurnitureSubCategoryChoices: str = None
    VehicleSubCategoryChoices: str = None
    sex: str = None
    size: str = None
    age: str = None
    # is_favourite: bool
    # it_bought: bool


# all doctors
class Display_doctor(Schema):
    full_name: str

    Specialization: str
    cv: str
    phone_number: str
    sunday: str
    monday: str
    tuesday: str
    wednesday: str
    thursday: str
    friday: str
    saturday: str
#-----------------------------------

class User_Info(Schema):
    # username: str
    email: str



class Display_Item(Schema):
    user: User_Info
    product: Display_product
    item_qty: int
    ordered: bool


class Display_Address(Schema):
    city: str
    home_address: str
    work_address: str
    phone: str





class Display_Order(Schema):
    user: User_Info
    address: Display_Address = None
    status: str
    note: str
    ref_code: str
    ordered: bool
    items: Display_Item



class OrderIn(Schema):
    status_id : int
    note: str = None
    ref_code : str
    ordered: bool
    address_id: int
    items_id: list[int]





class Rating_In(Schema):
    product_id: int
    value  : int
    comment: str




class Profile(Schema):
    name: str
    user: User_Info
    phone_number: str
    city: str





class Fav(Schema):
    product_id: int




class display_fav_prod(Schema):
    user: User_Info
    product: Display_product




class Card_Info(Schema):
    product_id: int




class display_card(Schema):
    user: User_Info
    product: Display_product





class qu(Schema):
    product_id: int