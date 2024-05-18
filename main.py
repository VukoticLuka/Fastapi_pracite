from fastapi import FastAPI
from sqlmodel import SQLModel

from databases.database import engine
from routers import user

app = FastAPI()

app.include_router(user.router)

SQLModel.metadata.create_all(engine)
