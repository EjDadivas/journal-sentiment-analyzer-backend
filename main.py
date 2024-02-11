import os
from typing import Optional, List

from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response
from pydantic import ConfigDict, BaseModel, Field, EmailStr
from pydantic.functional_validators import BeforeValidator

from typing_extensions import Annotated, Optional, Any

from bson import ObjectId
import motor.motor_asyncio
from pymongo import ReturnDocument

from dotenv import load_dotenv
import os

from transformers import RobertaTokenizerFast, TFRobertaForSequenceClassification, pipeline

tokenizer = RobertaTokenizerFast.from_pretrained("arpanghoshal/EmoRoBERTa")
model = TFRobertaForSequenceClassification.from_pretrained("arpanghoshal/EmoRoBERTa")

emotion = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, return_all_scores=True)


# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Journal Analysis System",
    summary="A Sentiment Analysis API for Journals",
)
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.journal_sentimentdb
journal_collection = db.get_collection("journal_entries")

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

# TODO: Define the needed fields for the JournalModel

class JournalModel(BaseModel):
    """
    Container for a single student record.
    """

    # The primary key for the StudentModel, stored as a `str` on the instance.
    # This will be aliased to `_id` when sent to MongoDB,
    # but provided as `id` in the API requests and responses.
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str = Field(...)
    # email: EmailStr = Field(...)
    entry: str = Field(...)
    # gpa: float = Field(..., le=4.0)
    sentiment_score: Optional[Any] 
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders = {ObjectId: str},
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "title": "My Journal",
                "entry": "This is my journal entry"
            }
        },
    )


class UpdateJournalModel(BaseModel):
    """
    A set of optional updates to be made to a document in the database.
    """

    title: Optional[str] = None
    # email: Optional[EmailStr] = None
    entry: Optional[str] = None
    # gpa: Optional[float] = None
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str},
        json_schema_extra={
            "example": {
                "title": "This is Updated Journal Title",
                # "email": "jdoe@example.com",
                "entry": "Experiments, Science, and Fashion in Nanophotonics",
                # "gpa": 3.0,
            }
        },
    )


class JournalCollection(BaseModel):
    """
    A container holding a list of `StudentModel` instances.

    This exists because providing a top-level array in a JSON response can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    journal_entries: List[JournalModel]


@app.post(
    "/journal_entries/",
    response_description="Add new entry",
    response_model=JournalModel,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_journal_entry(journal_entry: JournalModel = Body(...)):
    emotion_labels = emotion(journal_entry.entry)
    print(emotion_labels)

    # Create a new dictionary with all the fields from the journal_entry plus the sentiment_score
    journal_entry_dict = journal_entry.dict(by_alias=True, exclude={"id"})
    journal_entry_dict["sentiment_score"] = emotion_labels

    new_journal_entry = await journal_collection.insert_one(journal_entry_dict)
    created_journal_entry = await journal_collection.find_one(
        {"_id": new_journal_entry.inserted_id}
    )
    return journal_entry


@app.get(
    "/journal_entries/",
    response_description="List all journal entries",
    response_model=JournalCollection,
    response_model_by_alias=False,
)
async def list_journal_entries():
    """
    List all of the student data in the database.

    The response is unpaginated and limited to 1000 results.
    """
    return JournalCollection(journal_entries=await journal_collection.find().to_list(1000))


@app.get(
    "/journal_entry/{id}",
    response_description="Get a single student",
    response_model=JournalModel,
    response_model_by_alias=False,
)
async def show_journal_entry(id: str):
    """
    Get the record for a specific student, looked up by `id`.
    """
    if (
        journal_entry := await journal_collection.find_one({"_id": ObjectId(id)})
    ) is not None:
        return journal_entry

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.put(
    "/journal_entry/{id}",
    response_description="Update a journal entry",
    response_model=JournalModel,
    response_model_by_alias=False,
)
async def update_journal(id: str, journal_entry: UpdateJournalModel = Body(...)):
    """
    Update individual fields of an existing journal_entry record.

    Only the provided fields will be updated.
    Any missing or `null` fields will be ignored.
    """
    journal_entry = {
        k: v for k, v in journal_entry.model_dump(by_alias=True).items() if v is not None
    }

    if len(journal_entry) >= 1:
        update_result = await journal_collection.find_one_and_update(
            {"_id": ObjectId(id)},
            {"$set": journal_entry},
            return_document=ReturnDocument.AFTER,
        )
        if update_result is not None:
            return update_result
        else:
            raise HTTPException(status_code=404, detail=f"Journal {id} not found")

    # The update is empty, but we should still return the matching document:
    if (existing_journal_entry := await journal_collection.find_one({"_id": id})) is not None:
        return existing_journal_entry

    raise HTTPException(status_code=404, detail=f"Journal {id} not found")


@app.delete("/journal/{id}", response_description="Delete a journal")
async def delete_journal(id: str):
    """
    Remove a single student record from the database.
    """
    delete_result = await journal_collection.delete_one({"_id": ObjectId(id)})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")