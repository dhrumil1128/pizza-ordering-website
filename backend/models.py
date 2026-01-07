from pydantic import BaseModel
from typing import List

class CustomerInfo(BaseModel):
    name: str
    address: str

class OrderItem(BaseModel):
    pizza_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_info: CustomerInfo
    items: List[OrderItem]