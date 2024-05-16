from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str | None
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str | None

    class Config:
        from_attributes = True
