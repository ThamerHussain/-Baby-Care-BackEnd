from ninja import Schema


# all product
class Display_product(Schema):
    name: str
    description: str
    price: str
    image: str
    stars: int
    category: str
    ClotheSubCategoryChoices: str
    FoodSubCategoryChoices: str
    FoodToolSubCategoryChoices: str
    ShowerToolSubCategoryChoices: str
    VehicleSubCategoryChoices: str
    ContainerSubCategoryChoices: str
    FurnitureSubCategoryChoices: str
    VehicleSubCategoryChoices: str
    sex: str
    size: str
    age: str
    is_favourite: bool
    it_bought: bool


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