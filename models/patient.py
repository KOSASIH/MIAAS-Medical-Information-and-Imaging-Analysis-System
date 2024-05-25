from datetime import datetime
from typing import List

from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str = None
    address: str = None
    created_at: datetime

    class Config:
        orm_mode = True

    def __repr__(self):
        return f"<Patient(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email})>"


class PatientCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str = None
    address: str = None


class PatientUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    address: str = None
