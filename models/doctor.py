from datetime import datetime
from typing import List

from pydantic import BaseModel

class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str = None
    address: str = None
    specialty: str
    hospital_id: int
    created_at: datetime

    class Config:
        orm_mode = True

    def __repr__(self):
        return f"<Doctor(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, specialty={self.specialty})>"

class DoctorCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str = None
    address: str = None
    specialty: str
    hospital_id: int

class DoctorUpdate(BaseModel):
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    address: str = None
    specialty: str = None
    hospital_id: int = None
