from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response
from typing import List
import json
from bson import ObjectId, json_util
from pymongo import ReturnDocument
from app.models.journal import JournalModel
from app.database import journal_collection, student_collection
from app.services.sentiment_analysis import sentiment_analysis
from datetime import datetime
from collections import defaultdict
import logging

class JSONEncoder(json.JSONEncoder):
    def default(self, o):   
        return json_util.default(o)

router = APIRouter()
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def determine_sentiment_category(sentiment_scores):
    """
    Determine the sentiment category based on sentiment scores.
    """
    positive_score = sum(score['score'] for score in sentiment_scores if score['label'] in ['joy', 'surprise'])
    negative_score = sum(score['score'] for score in sentiment_scores if score['label'] in ['sadness', 'anger', 'fear'])

    logger.info(f"Positive Score: {positive_score}, Negative Score: {negative_score}")

    if positive_score > negative_score:
        return "positive"
    elif negative_score > positive_score:
        return "negative"
    else:
        return "neutral"

@router.post(
    "/",
    response_description="Add new entry: (title, entry, student_id only)",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_journal_entry(journal_entry: JournalModel = Body(...)):
    sentiment_score = sentiment_analysis(journal_entry.entry)
    sentiment_category = determine_sentiment_category(sentiment_score)
    
    try:
        result = await journal_collection.insert_one({
            "title": journal_entry.title,
            "entry": journal_entry.entry,
            "student_id": ObjectId(journal_entry.student_id),
            "sentiment_score": sentiment_score,
            "sentiment_category": sentiment_category,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        })
        new_journal_entry = await journal_collection.find_one({"_id": ObjectId(result.inserted_id)})
        new_journal_entry["_id"] = str(new_journal_entry["_id"])

        student = await student_collection.find_one({"_id": new_journal_entry["student_id"]})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]
            new_journal_entry["student_details"] = student
            del new_journal_entry["student_id"]
    except Exception as e:
        raise HTTPException(status_code=400, detail="An error occurred while creating the journal entry.")

    return new_journal_entry


@router.get(
    "/",
    response_description="List all journal entries",
    response_model_by_alias=False,
)
async def list_journal_entries():
    journal_entries = await journal_collection.find().to_list(1000)
    
    for journal_entry in journal_entries:
        journal_entry["_id"] = str(journal_entry["_id"])
        
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]
            journal_entry["student_details"] = student
        del journal_entry["student_id"]
        
        # Determine sentiment category
        sentiment_category = determine_sentiment_category(journal_entry["sentiment_score"])
        journal_entry["sentiment_category"] = sentiment_category

    return journal_entries

@router.get("/emotions", response_description="Get students with positive emotions")
async def get_students_with_positive_emotions():
    journal_entries = await journal_collection.find().to_list(1000)
    students_grouped_by_emotion = defaultdict(dict)

    for journal_entry in journal_entries:
        for emotion in journal_entry["sentiment_score"]:
            emotion_score = round(emotion["score"], 2)
            if emotion_score > 0:
                student_id = journal_entry["student_id"]
                if student_id in students_grouped_by_emotion[emotion["label"]]:
                    students_grouped_by_emotion[emotion["label"]][student_id]["emotion_score"] += emotion_score
                else:
                    student = await student_collection.find_one({"_id": ObjectId(student_id)})
                    if student:
                        student["_id"] = str(student["_id"])
                        del student["password"]
                        student["emotion_score"] = emotion_score
                        students_grouped_by_emotion[emotion["label"]][student_id] = student

    # Convert the inner dictionaries to lists
    for emotion, students in students_grouped_by_emotion.items():
        students_grouped_by_emotion[emotion] = list(students.values())

    return dict(students_grouped_by_emotion)

@router.get(
    "/{id}",
    response_description="Get a single journal entry",
    response_model_by_alias=False,
)
async def show_journal_entry(id: str):
    if (
        journal_entry := await journal_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        journal_entry["_id"] = str(journal_entry["_id"])
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]
            journal_entry["student_details"] = student
        del journal_entry["student_id"]
        
        # Determine sentiment category
        sentiment_category = determine_sentiment_category(journal_entry["sentiment_score"])
        journal_entry["sentiment_category"] = sentiment_category
        
        return journal_entry

    raise HTTPException(status_code=404, detail=f"Journal entry {id} not found")

@router.get("/student/{student_id}", response_description="Get journal entries by student ID")
async def get_journals_by_student_id(student_id: str):
    journal_entries = await journal_collection.find({"student_id": ObjectId(student_id)}).to_list(1000)
    for journal_entry in journal_entries:
        journal_entry["_id"] = str(journal_entry["_id"])
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]
            journal_entry["student_details"] = student
        del journal_entry["student_id"] 
        
        # Determine sentiment category
        sentiment_category = determine_sentiment_category(journal_entry["sentiment_score"])
        journal_entry["sentiment_category"] = sentiment_category
        
    return journal_entries

@router.patch("/{id}",
    response_description="Update a journal entry (only the title and entry can be updated)",
    response_model_by_alias=False,
)
async def update_journal(id: str, journal_entry: JournalModel = Body(...)):
    
    sentiment_score = sentiment_analysis(journal_entry.entry)
    sentiment_category = determine_sentiment_category(sentiment_score)
    
    update_result = await journal_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {
            "entry": journal_entry.entry,
            "title": journal_entry.title,
            "sentiment_score": sentiment_score,
            "sentiment_category": sentiment_category,
            "updated_at": datetime.utcnow(),
            }
         },
        return_document=ReturnDocument.AFTER,
    )
    if update_result is not None:
        update_result["_id"] = str(update_result["_id"])
        update_result["student_id"] = str(update_result["student_id"])
        
        # Update sentiment category
        update_result["sentiment_category"] = sentiment_category 
        return update_result

    if (existing_journal_entry := await journal_collection.find_one({"_id": ObjectId(id)})) is not None:
        return existing_journal_entry

    raise HTTPException(status_code=404, detail=f"Journal entry {id} not found")

@router.delete("/{id}", response_description="Delete a journal")
async def delete_journal(id: str):
    delete_result = await journal_collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Journal entry {id} not found")