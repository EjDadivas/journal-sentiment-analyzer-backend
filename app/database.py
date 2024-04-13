import motor.motor_asyncio
from pymongo import ReturnDocument
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
print("mongodb url: ", os.getenv("MONGODB_URL"))
print( os.getenv("MONGODB_URL"))
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL")) 

db = client.journal_sentimentdb

journal_collection = db.get_collection("journal_entries")
student_collection = db.get_collection("students")
admin_collection = db.get_collection("admins")

