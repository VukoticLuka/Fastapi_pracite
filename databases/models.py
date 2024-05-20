from sqlmodel import SQLModel, Field


class DbUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str | None = None
    password: str
