from datetime import datetime

from pydantic import BaseModel, ConfigDict


class UserRequest(BaseModel):
    username : str
    email :str
    full_name : str
    is_active:bool = True

class UserUpdate(BaseModel):
    username: str | None = None
    email: str | None = None
    full_name: str | None = None


class UserResponse(BaseModel):
    id:int
    username : str
    email :str
    full_name : str
    is_active:bool 
    created_at : datetime

    model_config = ConfigDict(from_attributes=True)
