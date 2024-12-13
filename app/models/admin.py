from typing import Optional, Any
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
from bson import ObjectId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class AdminModel(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    password: str
    journal_pin: Optional[str] = None 

    @validator("password")
    def hash_password(cls, password: str) -> str:
        return pwd_context.hash(password)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "firstName": "Admin",
                "lastName": "User",
                "email": "admin@school.com",
                "password": "admin123",
                "journal_pin": "123456",  
            }
        }