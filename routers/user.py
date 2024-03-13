from typing import List

from fastapi import APIRouter
from db import users, database
from models import User, UserIn

router = APIRouter()


@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(firstname=user.firstname, lastname=user.lastname,
                                  email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "user_id": last_record_id}


@router.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.user_id == user_id)
    return await database.fetch_one(query)


@router.put("/users/{user_id}", response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.user_id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), "user_id": user_id}


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.user_id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}