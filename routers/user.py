from typing import List

from fastapi import APIRouter
from databases import db_user
from schemas import UserBase, UserDisplay

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.post('/new', response_model=UserDisplay)
async def create_user(request: UserBase):
    return await db_user.create_user(request)


@router.get('/all', response_model=List[UserDisplay])
async def get_all_users():
    return await db_user.get_all_users()


@router.get('/{id}', response_model=UserDisplay)
async def get_user(id: int):
    return await db_user.get_user(id)


@router.put('/update/{id}')
async def update_user(id: int, request: UserBase):
    return db_user.update_user(id, request)
