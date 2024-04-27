from fastapi import APIRouter, Body, HTTPException
from app.models.admin import AdminModel
from app.database import admin_collection
from app.models.admin import pwd_context
from bson import ObjectId

router = APIRouter()

@router.post("/register", response_description="Add new admin")
async def register_admin(admin: AdminModel = Body(...)):
    result = await admin_collection.insert_one(admin.dict())
    new_admin = await admin_collection.find_one({"_id": result.inserted_id})
    new_admin["_id"] = str(new_admin["_id"])
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

@router.get("/{id}", response_description="Get a single admin")
async def get_admin(id: str):
    if (admin := await admin_collection.find_one({"_id": ObjectId(id)})) is not None:
        admin["_id"] = str(admin["_id"])

        return admin

    raise HTTPException(status_code=404, detail=f"Admin {id} not found")