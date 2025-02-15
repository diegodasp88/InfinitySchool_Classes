import db
from fastapi import FastAPI, HTTPException, status
from models import Product
from schema import ProductInput, ProductOutput, MessageOut


app = FastAPI(
    title="Inventory Control", 
    description="API to control the inventory of products."
)


# Creating products
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_new_product(product: ProductInput) -> MessageOut:
    new_product = Product(**product.model_dump())
    db.create_new_product(new_product)
    product.id += 1
    return MessageOut(message="Product created successfully.")


# Looking for products
@app.get("/products")
def get_products() -> list[ProductOutput]:
    products = db.get_all_products()
    if len(products) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
    return products