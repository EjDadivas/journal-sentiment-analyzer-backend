from fastapi import APIRouter, Body, HTTPException, status
from typing import List
from app.models.student import Student
from app.database import student_collection

router = APIRouter()

#TODO: Login Endpoint

@router.post("/", response_description="Add new student", response_model=Student)
async def create_student(student: Student = Body(...)):
    student = await student_collection.insert_one(student.dict())
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return new_student

@router.get("/", response_description="List all students", response_model=List[Student])
async def list_students():
    students = await student_collection.find().to_list(1000)
    return students

@router.get("/{id}", response_description="Get a single student", response_model=Student)
async def show_student(id: str):
    if (student := await student_collection.find_one({"_id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@router.put("/{id}", response_description="Update a student", response_model=Student)
async def update_student(id: str, student: Student = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}

    if len(student) >= 1:
        update_result = await student_collection.update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (
                updated_student := await student_collection.find_one({"_id": id})
            ) is not None:
                return updated_student

    if (existing_student := await student_collection.find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")

@router.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await student_collection.delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")