from typing import Union, Optional

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Student(BaseModel):
    name: str
    surname: str
    age: int
    email: str

def fetch_students() -> [Student]:
    return [Student(name="John", surname="Smith", age=17, email="test@example.com")]

@app.get("/students")
async def list_students():
    return fetch_students()

def start():
    """Launched with `poetry run start` at root level"""
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
