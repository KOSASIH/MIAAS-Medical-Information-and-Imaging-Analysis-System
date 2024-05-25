from datetime import datetime
from typing import List

from pydantic import BaseModel

class Hospital(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    zip: str
    created_at: datetime

    class Config:
        orm_mode = True

    def __repr__(self):
        return f"<Hospital(id={self.id}, name={self.name}, address={self.address}, city={self.city}, state={self.state}, zip={self.zip})>"

class HospitalCreate(BaseModel):
    name: str
    address: str
    city: str
    state: str
    zip: str

class HospitalUpdate(BaseModel):
    name: str = None
    address: str = None
    city: str = None
    state: str = None
    zip: str = None
