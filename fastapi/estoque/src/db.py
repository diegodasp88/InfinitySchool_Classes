from models import Product
from tinydb import TinyDB

db = TinyDB("./database.json", indent=2)

def get_all_products() -> list[Product]:
    # Getting all products inserted on db table.
    products = db.table("products").all()
    return [Product(**product) for product in products]


def create_new_product(product: Product) -> None:
    # Creating the product profile and converting it into a Python Dict.
    product_profile = product.model_dump()
    # Updating values so that it can be saved on a JSON file.
    product_profile.update({"created_at": product.created_at.isoformat()})
    # Adding the product profile to the db table.
    db.table("products").insert(product_profile)