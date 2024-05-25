from typing import List

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/patients", tags=["Patients"])


class Patient(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str


patients_data = [
    Patient(
        id=1,
        first_name="John",
        last_name="Doe",
        email="johndoe@example.com",
        phone="123-456-7890",
        address="123 Main St, Anytown, USA",
    ),
    Patient(
        id=2,
        first_name="Jane",
        last_name="Smith",
        email="janesmith@example.com",
        phone="987-654-3210",
        address="456 Elm St, Othertown, USA",
    ),
    # Add more patient data here
]


@router.get("/", response_model=List[Patient])
async def read_patients():
    return patients_data


@router.get("/{patient_id}", response_model=Patient)
async def read_patient(patient_id: int):
    patient = next((p for p in patients_data if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.post("/", response_model=Patient)
async def create_patient(patient: Patient):
    patients_data.append(patient)
    return patient


@router.put("/{patient_id}", response_model=Patient)
async def update_patient(patient_id: int, patient: Patient):
    patient_idx = next(
        (i for i, p in enumerate(patients_data) if p.id == patient_id), None
    )
    if patient_idx is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients_data[patient_idx] = patient
    return patient


@router.delete("/{patient_id}")
async def delete_patient(patient_id: int):
    patient_idx = next(
        (i for i, p in enumerate(patients_data) if p.id == patient_id), None
    )
    if patient_idx is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients_data[patient_idx]
    return {"message": "Patient deleted"}
