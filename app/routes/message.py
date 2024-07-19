from fastapi import APIRouter, Body, WebSocket, HTTPException, status, Query
from typing import List, Optional
from app.models.message import MessageHistoryModel
from app.database import message_collection
from bson import ObjectId
import json
from datetime import datetime

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
from fastapi import WebSocketDisconnect

@router.websocket("/{user_id}/ws")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            message_data['created_at'] = datetime.fromisoformat(message_data['created_at'].replace("Z", "+00:00"))
            message = MessageHistoryModel(**message_data)
            await message_collection.insert_one(message.dict(by_alias=True))
            await websocket.send_text(message.message)
    except WebSocketDisconnect:
        print(f"WebSocket connection with user {user_id} closed")