from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponseSchema(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    class Config:
        orm_mode = True
        fields = {
            "id": "_id"
        }

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserUpdateSchema(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    password: Optional[str]