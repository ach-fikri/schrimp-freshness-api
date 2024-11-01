from typing import Optional
from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    id: Optional[str]
    name: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
        fields = {
            "id": "_id"
        }