from fastapi import APIRouter, Body, WebSocket, HTTPException, status, Query
from typing import List, Optional
from app.models.message import MessageHistoryModel
from app.database import message_collection
from bson import ObjectId
import json
from datetime import datetime

router = APIRouter()

@router.get("/{sender_id}", response_description="Get all messages sent by a user")
async def get_messages_sent_by(sender_id: str):
    messages = await message_collection.find({"sender_id": sender_id}).to_list(1000)
    for message in messages:
        message["_id"] = str(message["_id"])
        message["created_at"] = message["created_at"].isoformat() if isinstance(message["created_at"], datetime) else message["created_at"]
    return messages

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

class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, user_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[user_id] = websocket

    async def disconnect(self, user_id: str):
        del self.active_connections[user_id]


    async def send_personal_message(self, message: dict, user_id: str):
        message_str = json.dumps(message)
        print("message_str", message_str)
        print("user_id", user_id)
        if user_id in self.active_connections:
            try:
                await self.active_connections[user_id].send_text(message_str)
            except Exception as e:
                print(f"Failed to send message to user {user_id}: {e}")
        else:
            print(f"User {user_id} is not connected. Message saved but not sent.")


manager = ConnectionManager()
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(user_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            message_data['created_at'] = datetime.fromisoformat(message_data['created_at'].replace("Z", "+00:00"))
            message = MessageHistoryModel(**message_data)
            await message_collection.insert_one(message.dict(by_alias=True))
            message_data['created_at'] = message.created_at.isoformat()
            await manager.send_personal_message(message_data, user_id)
            await manager.send_personal_message(message_data, message.receiver_id)
    except WebSocketDisconnect:
        manager.disconnect(user_id)
        print(f"WebSocket connection with user {user_id} closed")