from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session, select, update, delete

from databases.database import engine
from databases.models import DbUser
from schemas import UserBase


async def create_user(request: UserBase):
    with Session(engine) as session:
        user = DbUser(
            username=request.username, email=request.email, password=request.password
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


async def get_all_users():
    with Session(engine) as session:
        return session.exec(select(DbUser)).all()


def update_user(id: int, request: UserBase):
    with Session(engine) as session:
        user = session.query(DbUser).filter(DbUser.id == id)
        if not user.first():
            raise HTTPException(status_code=404, detail="User not found")
        user.update(
            {
                DbUser.username: request.username,
                DbUser.email: request.email,
                DbUser.password: request.password,
            }
        )
        session.commit()
        return {"msg": "Ok"}


def delete_user(id: int):
    with Session(engine) as session:
        user = session.get(DbUser, id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        session.delete(user)
        session.commit()
        return user