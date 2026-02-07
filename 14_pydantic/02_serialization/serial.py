from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v:v.strftime('%d-%m-%Y  %H:%M:%S')}
    )

user = User(
    id=1,
    name="Kalyan",
    email="kalyan@gmail.com",
    createdAt=datetime(2025, 3, 15, 14, 30, 20),
    address=Address(
        city="ATP",
        street="Akp",
        zip_code="515001",
    
    ),
    is_active= False,
    tags=["Premier", "Subscriber" ]
)

python_disc = user.model_dump()
print(user)
print("="*30)
print(python_disc)

json_str = user.model_dump_json()
print("-->"*30)
print(json_str)