from fastapi import APIRouter, Body, HTTPException, status
from fastapi.responses import Response
from fastapi.encoders import jsonable_encoder
from typing import List
import json
from bson import ObjectId, json_util
from pymongo import ReturnDocument
from app.models.journal import JournalModel
from app.database import journal_collection
from app.services.sentiment_analysis import sentiment_analysis

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        return json_util.default(o)
    
router = APIRouter()

@router.post(
    "/",
    response_description="Add new entry",
    # response_model=JournalModel, TODO: Fix response model error
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_journal_entry(journal_entry: JournalModel = Body(...)):
    sentiment_score = sentiment_analysis(journal_entry.entry)

    try:
        result = await journal_collection.insert_one({
            "title": journal_entry.title,
            "entry": journal_entry.entry,
            "student_id": ObjectId(journal_entry.student_id),
            "sentiment_score": sentiment_score
        })
        new_journal_entry = await journal_collection.find_one({"_id": result.inserted_id})
    except Exception as e:
        raise HTTPException(status_code=400, detail="An error occurred while creating the journal entry.")
    # TODO: FIx return
    return {"status": "success"}

@router.get(
    "/",
    response_description="List all journal entries",
    response_model=List[JournalModel],
    response_model_by_alias=False,
)
async def list_journal_entries():
    journal_entries = await journal_collection.find().to_list(1000)
    return journal_entries

@router.get(
    "/{id}",
    response_description="Get a single journal entry",
    response_model=JournalModel,
    response_model_by_alias=False,
)
async def show_journal_entry(id: str):
    if (
        journal_entry := await journal_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return journal_entry

    raise HTTPException(status_code=404, detail=f"Journal entry {id} not found")

@router.put(
    "/{id}",
    response_description="Update a journal entry",
    response_model=JournalModel,
    response_model_by_alias=False,
)
@router.put(
    "/{id}",
    response_description="Update a journal entry",
    response_model=JournalModel,
    response_model_by_alias=False,
)
async def update_journal(id: str, journal_entry: JournalModel = Body(...)):
    journal_entry = {
        k: v for k, v in journal_entry.dict(by_alias=True).items() if v is not None
    }

    if len(journal_entry) >= 1:
        update_result = await journal_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": journal_entry},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
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