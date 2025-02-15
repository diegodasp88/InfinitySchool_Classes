from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field


class Category(StrEnum):
    FOOD = "ALIMENTO"
    CLEANING = "LIMPEZA"
    HYGIENE = "HIGIENE"
    ELECTRONICS = "ELETRONICO"

class Product(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    category: Category
    quantity: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
