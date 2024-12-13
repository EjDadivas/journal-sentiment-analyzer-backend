from fastapi import APIRouter, Body, HTTPException
from app.models.admin import AdminModel
from app.database import admin_collection
from app.models.admin import pwd_context
from bson import ObjectId
from pydantic import BaseModel, Field

router = APIRouter()

class JournalPinModel(BaseModel):
    pin: str = Field(..., min_length=6, max_length=6, pattern=r'^\d{6}$')

@router.post("/register", response_description="Add new admin")
async def register_admin(admin: AdminModel = Body(...)):
    result = await admin_collection.insert_one(admin.dict())
    new_admin = await admin_collection.find_one({"_id": result.inserted_id})
    new_admin["_id"] = str(new_admin["_id"])
    del new_admin["password"] 
    return new_admin

@router.post("/login", response_description="Login an admin")
async def login_admin(email: str = Body(...), password: str = Body(...)):
    admin = await admin_collection.find_one({"email": email})
    if not admin:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not pwd_context.verify(password, admin["password"]):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    admin["_id"] = str(admin["_id"])
    del admin["password"] 
    return admin

@router.get("/", response_description="List all admins")
async def list_admins():
    admins = await admin_collection.find().to_list(1000)
    for admin in admins:
        admin["_id"] = str(admin["_id"])
        del admin["password"]        
    return admins

@router.get("/{id}", response_description="Get a single admin")
async def get_admin(id: str):
    if (admin := await admin_collection.find_one({"_id": ObjectId(id)})) is not None:
        admin["_id"] = str(admin["_id"])
        return admin
    raise HTTPException(status_code=404, detail=f"Admin {id} not found")

@router.get("/journal-pin/{id}", response_description="Get the journal pin for a specific admin")
async def get_journal_pin(id: str):
    admin = await admin_collection.find_one({"_id": ObjectId(id)}, {"journal_pin": 1})
    if admin and "journal_pin" in admin:
        return {"journal_pin": admin["journal_pin"]}
    raise HTTPException(status_code=404, detail=f"Journal pin not found for admin {id}")


@router.post("/add-journal-pin", response_description="Add a journal pin")
async def add_journal_pin(pin: JournalPinModel = Body(...)):
    await admin_collection.update_many(
        {}, 
        {"$set": {"journal_pin": pin.pin}}
    )
    return {"message": "Journal pin added successfully to all admins"}

@router.put("/update-journal-pin", response_description="Update the journal pin")
async def update_journal_pin(pin: JournalPinModel = Body(...)):
    await admin_collection.update_many(
        {}, 
        {"$set": {"journal_pin": pin.pin}}
    )
    return {"message": "Journal pin updated successfully for all admins"}

@router.delete("/delete-journal-pin", response_description="Delete the journal pin")
async def delete_journal_pin():
    await admin_collection.update_many(
        {}, 
        {"$unset": {"journal_pin": ""}}
    )
    return {"message": "Journal pin deleted successfully for all admins"}


