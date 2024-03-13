from datetime import datetime

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    user_id: int
    firstname: str = Field(..., title='first name', max_length=50)
    lastname: str = Field(..., title='last name', max_length=100)
    email: EmailStr = Field(..., title='emai', max_length=120)


class UserIn(User):
    password: str = Field(..., title='password', min_length=6, max_length=15)



class ProductIn(BaseModel):
    title: str = Field(..., title='title', max_length=100)
    description: str = Field(default='', title='description', max_length=200)
    price: float = Field(..., title='price', gt=0, le=10_000)


class Product(ProductIn):
    prod_id: int


class OrderIn(BaseModel):
    user_id: int = Field(..., title='user_id')
    prod_id: int = Field(..., title='prod_id')
    date: datetime.date = Field(..., title='date')
    status: bool = False


class Order(OrderIn):
    order_id: int
    firstname: str
    lastname: str
    email: EmailStr
    title: str
    description: str
    price: float