from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional


class User(Document):
    user_id:UUID = Field(default_factory=uuid4)
    username: Indexed(str, unique=True)
    email: Indexed(EmailStr, unique=True)
    hash_password: str
    first_name:Optional[str] = None
    last_name: Optional[str] = None
    disabled:Optional[bool] = None

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self):
        return self.email
    def __hash__(self)->int:
        return hash(self.email)

    def __eq__(self,other:object)-> boll:
        if isinstance(other,User):
            return self.email == other.email
        return False
    

