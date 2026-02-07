from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True #default

product_one = Product(id= 1, name="Mobile", price="24543.23", in_stock= False)
product_two = Product(id= 2, name="Earbuds", price="24543.23") 

print(product_one, product_two)
