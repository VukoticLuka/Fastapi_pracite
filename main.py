from fastapi import FastAPI
from sqlmodel import SQLModel

from databases.database import engine


app = FastAPI()

SQLModel.metadata.create_all(engine)