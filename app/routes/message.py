from fastapi import APIRouter, Body, WebSocket, HTTPException, status
from typing import List
from app.models.message import MessageHistoryModel
from app.database import message_collection
from bson import ObjectId
import json

router = APIRouter()

@router.get("/", response_description="Load chat history")
async def load_chat_history(sender_id: str, receiver_id: str):
    messages = await message_collection.find({
        "$or": [
            {"sender_id": sender_id, "receiver_id": receiver_id},
            {"sender_id": receiver_id, "receiver_id": sender_id}
        ]
    }).to_list(1000) 
    for message in messages:
        message["_id"] = str(message["_id"])
    return messages

@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        message_data = json.loads(data)
        message = MessageHistoryModel(**message_data)
        await message_collection.insert_one(message.dict(by_alias=True))
        await websocket.send_text(message.message)
