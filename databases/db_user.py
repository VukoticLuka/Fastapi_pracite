from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from databases.database import engine
from databases.models import DbUser
from schemas import UserBase


async def create_user(request: UserBase):
    with Session(engine) as session:
        user = DbUser(
            username=request.username,
            email=request.email,
            password=request.password
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


async def get_user(id: int) -> Optional[DbUser]:
    with Session(engine) as session:
        result = session.exec(select(DbUser).where(DbUser.id == id))
        user = result.first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
