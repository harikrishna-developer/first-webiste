from fastapi import FastAPI

from app.database import Base, engine
from app.models import User  # noqa: F401
from app.routers import user_router

print("Registered tables:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router.router)