from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/doctors", tags=["Doctors"])

class Doctor(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    specialty: str

doctors_data = [
    Doctor(id=1, first_name="Dr. John", last_name="Smith", email="drjohnsmith@example.com", phone="555-123-4567", address="789 Oak St, Anytown, USA", specialty="Cardiology"),
    Doctor(id=2, first_name="Dr. Jane", last_name="Doe", email="drjanedoe@example.com", phone="555-987-6543", address="321 Maple St, Othertown, USA", specialty="Neurology"),
    # Add more doctor data here
]

@router.get("/", response_model=List[Doctor])
async def read_doctors():
    return doctors_data

@router.get("/{doctor_id}", response_model=Doctor)
async def read_doctor(doctor_id: int):
    doctor = next((d for d in doctors_data if d.id == doctor_id), None)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@router.post("/", response_model=Doctor)
async def create_doctor(doctor: Doctor):
    doctors_data.append(doctor)
    return doctor

@router.put("/{doctor_id}", response_model=Doctor)
async def update_doctor(doctor_id: int, doctor: Doctor):
    doctor_idx = next((i for i, d in enumerate(doctors_data) if d.id == doctor_id), None)
    if doctor_idx is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctors_data[doctor_idx] = doctor
    return doctor

@router.delete("/{doctor_id}")
async def delete_doctor(doctor_id: int):
    doctor_idx = next((i for i, d in enumerate(doctors_data) if d.id == doctor_id), None)
    if doctor_idx is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    del doctors_data[doctor_idx]
    return {"message": "Doctor deleted"}
