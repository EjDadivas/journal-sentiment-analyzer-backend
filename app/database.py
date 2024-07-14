import motor.motor_asyncio
from pymongo import ReturnDocument, MongoClient
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
print("mongodb url: ", os.getenv("MONGODB_URL"))
print( os.getenv("MONGODB_URL"))
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGODB_URL"), tls=True, tlsAllowInvalidCertificates=True) 

db = client.journal_sentimentdb

journal_collection = db.get_collection("journal_entries")
student_collection = db.get_collection("students")
admin_collection = db.get_collection("admins")
message_collection = db.get_collection("message_history")

