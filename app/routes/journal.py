from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response
# from fastapi.encoders import jsonable_encoder
from typing import List
import json
from bson import ObjectId, json_util
from pymongo import ReturnDocument
from app.models.journal import JournalModel
from app.database import journal_collection, student_collection
from app.services.sentiment_analysis import sentiment_analysis
from datetime import datetime
class JSONEncoder(json.JSONEncoder):
    def default(self, o):   
        return json_util.default(o)
    
router = APIRouter()

@router.post(
    "/",
    response_description="Add new entry: (title, entry, student_id only)",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_journal_entry(journal_entry: JournalModel = Body(...)):
    sentiment_score = sentiment_analysis(journal_entry.entry)
    print(sentiment_score)
    try:
        result = await journal_collection.insert_one({
            "title": journal_entry.title,
            "entry": journal_entry.entry,
            "student_id": ObjectId(journal_entry.student_id),
            "sentiment_score": sentiment_score,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
            
        })
        new_journal_entry = await journal_collection.find_one({"_id": result.inserted_id})
        new_journal_entry["_id"] = str(new_journal_entry["_id"])
        del new_journal_entry["student_id"]
        
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["id"]
            del student["password"]  # remove the password before adding the student details
            new_journal_entry["student_details"] = student
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
        del journal_entry["student_id"]
          # Fetch the student details
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]  # remove the password before adding the student details
            journal_entry["student_details"] = student

    return journal_entries

@router.get(
    "/{id}",
    response_description="Get a single journal entry",
    # response_model=JournalModel,
    response_model_by_alias=False,
)
async def show_journal_entry(id: str):
    if (
        journal_entry := await journal_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        journal_entry["_id"] = str(journal_entry["_id"])
        del journal_entry["student_id"]
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]  # remove the password before adding the student details
            journal_entry["student_details"] = student
        
        return journal_entry

    raise HTTPException(status_code=404, detail=f"Journal entry {id} not found")



@router.get("/student/{student_id}", response_description="Get journal entries by student ID")
async def get_journals_by_student_id(student_id: str):
    journal_entries = await journal_collection.find({"student_id": ObjectId(student_id)}).to_list(1000)
    for journal_entry in journal_entries:
        journal_entry["_id"] = str(journal_entry["_id"])
        del journal_entry["student_id"] 
        student = await student_collection.find_one({"_id": ObjectId(journal_entry["student_id"])})
        if student:
            student["_id"] = str(student["_id"])
            del student["password"]  # remove the password before adding the student details
            journal_entry["student_details"] = student
    return journal_entries


@router.patch("/{id}",
    response_description="Update a journal entry (only the title and entry can be updated)",
    response_model_by_alias=False,
)
async def update_journal(id: str, journal_entry: JournalModel = Body(...)):
    
    sentiment_score = sentiment_analysis(journal_entry.entry)
    
    update_result = await journal_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": {
            "entry": journal_entry.entry,
            "title": journal_entry.title,
            "sentiment_score": sentiment_score,
            "updated_at": datetime.utcnow(),   
            }
         },
        return_document=ReturnDocument.AFTER,
    )
    if update_result is not None:
        print("update_result", update_result)
        update_result["_id"] = str(update_result["_id"])
        update_result["student_id"] = str(update_result["student_id"])
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