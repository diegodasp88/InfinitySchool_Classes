from datetime import datetime
from models import Category
from pydantic import BaseModel, Field

class MessageOut(BaseModel):
    message: str


class ProductInput(BaseModel):
    name: str
    description: str | None = None
    category: Category
    quantity: int = Field(default=0, ge=0) # "ge" means "Greater or Equal than"


class ProductOutput(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    category: Category
    quantity: int
    created_at: datetime