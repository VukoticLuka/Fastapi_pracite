from sqlmodel import Session

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
