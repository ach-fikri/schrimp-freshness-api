from beanie import Document
from pydantic import BaseModel, EmailStr


class User(Document):
    