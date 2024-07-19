from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class MessageHistoryModel(BaseModel):
    sender_id: str
    receiver_id: str
    message: str
    sender_type: str  # 'admin' or 'student'
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
        schema_extra = {
            "example": {
                "sender_id": "507f1f77bcf86cd799439011",
                "receiver_id": "507f1f77bcf86cd799439012",
                "message": "Hello, this is a test message.",
                "sender_type": "admin",
                "created_at": "2023-04-05T14:48:00.000Z"
            }
        }

