from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Person(BaseModel):
    f_name: str
    l_name: str

    @field_validator('f_name','l_name')
    def nameMustBeCaptilized(cls, v):
        if not v.istitle():
            raise ValueError("Name Must Be Capitalized.")
        return v

per1 = Person(f_name="Kalyan",l_name="Eswar")
print(per1)

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    
class Product(BaseModel):
    price: str # $4.5

    @field_validator('price', mode= 'before')
    def parse_proce(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',',''))
        return v

class DateRange(BaseModel):
    start_date: datetime
    end_time: datetime

    @model_validator(mode='after')
    def validateDateRange(cls, values):
        if values.start_date >= values.end_time:
            raise ValueError('End date must be after start date')
        return values
