from pydantic import BaseModel, field_validator
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    pascode: str

class User(BaseModel):
    name: str
    ph_num: int
    address: Address

address1 = Address(
    city="Anatapur",
    street="SK Univesity",
    pascode="525100",
)

user = User(
    name = "Kalyan",
    ph_num=123456789,
    address=address1
)

user_data = {
    "name" : "Kalyan",
    "ph_num":123456789,
    "address": {
        "city":"Anatapur",
        "street":"SK Univesity",
        "pascode":"525100"
    }
}

user = User(**user_data)
print(user)