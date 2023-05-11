from pydantic import BaseModel
from uuid import UUID

class StudentBase(BaseModel):
    name: str
    surname: str
    age: int
    email: str


class StudentDBBase(StudentBase):
    id: UUID

    class Config:
        orm_mode = True

class StudentWrite(StudentBase):
    pass

class Student(StudentDBBase):
    pass
