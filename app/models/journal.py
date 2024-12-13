from pydantic import BaseModel, Field
from typing import List, Optional, Annotated
from bson import ObjectId
from datetime import datetime
from pydantic.functional_validators import BeforeValidator


PyObjectId = Annotated[str, BeforeValidator(str)]
class SentimentScore(BaseModel):
    score: float
    label: str

class JournalModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    entry: str = Field(...)
    student_id: Optional[str] = Field(default=None)
    sentiment_scores: Optional[List[SentimentScore]] = []
    allow_admin_read: bool = Field(default=False) 


    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "title": "My Journal",
                "entry": "This is my journal entry",
                "student_id": "student1",
            }
        }