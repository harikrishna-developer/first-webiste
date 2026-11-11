from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User  # noqa: F401
from app.schemas.user import UserRequest, UserResponse, UserUpdate
from app.services.user_service import (
    create_user,
    delete_user_by_id,
    fetch_user_by_id,
    fetch_users,
    update_user_by_id,
)

router = APIRouter()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user_api(db: db_dependency, user_request: UserRequest):
    return create_user(db,user_request)

@router.get("/users", response_model=list[UserResponse])
async def fetch_users_api(db:db_dependency):

    return fetch_users(db)

@router.get("/users/{user_id}", response_model=UserResponse)
async def fetch_user_by_id_api(db:db_dependency, user_id:int):
    
    return fetch_user_by_id(db, user_id)

@router.patch("/users/{user_id}", response_model=UserResponse)
def update_user_by_id_api(
            db: db_dependency,
            user_id: int,
            user_update: UserUpdate
        ):
    return update_user_by_id(db, user_id, user_update)



@router.delete("/users/{user_id}")
def delete_user_by_id_api(
    db: db_dependency,
    user_id: int
):
    return delete_user_by_id(db, user_id)