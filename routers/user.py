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


@router.get('/{id}', response_model=UserDisplay)
async def get_user(id: int):
    return await db_user.get_user(id)
