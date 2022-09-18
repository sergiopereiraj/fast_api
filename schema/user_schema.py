from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    user_password: str

class DataUser(BaseModel):
    username: str
    user_password: str