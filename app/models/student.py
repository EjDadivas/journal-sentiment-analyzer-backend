from typing import Optional, Any
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
from bson import ObjectId

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Student(BaseModel):
    firstName: str
    lastName: str
    userName: str
    email: EmailStr
    course_of_study: str
    year: int
    password: str

    @validator("password")
    def hash_password(cls, password: str) -> str:
        return pwd_context.hash(password)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "firstName": "Abdulazeez",
                "lastName": "Abdulazeez Adeshina",
                "userName": "abdul",
                "email": "abdul@school.com",
                "course_of_study": "Water resources engineering",
                "year": 4,
                "password": "password123",
            }
        }

    class Settings:
        name = "student"