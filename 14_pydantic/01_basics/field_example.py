from pydantic import BaseModel
from typing import Dict, List, Optional

class Cart(BaseModel):
    user_id : int
    items: List[str]
    quantites: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url : Optional[str] = None

cart_data = {
    "user_id": 12,
    "items": ["Laptop", "Mouse", "Phone"],
    "quantites": {
        "Laptop": 2,
        "Mouse": 3, 
        "Phone": 5
    }
}

cart = Cart(**cart_data)
print(cart)