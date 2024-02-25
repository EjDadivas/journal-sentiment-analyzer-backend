import motor.motor_asyncio
from pymongo import ReturnDocument

from dotenv import load_dotenv
import os

client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.journal_sentimentdb

journal_collection = db.get_collection("journal_entries")
student_collection = db.get_collection("students")

