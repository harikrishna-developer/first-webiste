
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserRequest, UserUpdate


def create_user(
        db:Session,
        user_req:UserRequest):
    user = User(**user_req.model_dump())

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def fetch_users(
        db:Session
        ):
    users = db.query(User).all()
    return users

def fetch_user_by_id(db:Session,user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return user

def update_user_by_id(db:Session,
                      user_id:int,
                      update_request:UserUpdate
                      ):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    update_data = update_request.model_dump(exclude_unset=True)

    if "username" in update_data:
        user.username = update_data["username"]

    if "email" in update_data:
        user.email = update_data["email"]

    if "full_name" in update_data:
        user.full_name = update_data["full_name"]

    db.commit()
    db.refresh(user)
    return user


def delete_user_by_id(db:Session, user_id:int):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
