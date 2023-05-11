from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = Column(String)
    surname = Column(String)
    age = Column(Integer)
    email = Column(String)
