from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import journal, student, admin, message

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(journal.router, prefix="/journal", tags=["journal"])
app.include_router(student.router, prefix="/student", tags=["student"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(message.router, prefix="/message", tags=["message"])