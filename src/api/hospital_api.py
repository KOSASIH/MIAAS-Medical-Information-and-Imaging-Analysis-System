from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/hospitals", tags=["Hospitals"])

class Hospital(BaseModel):
    id: int
    name: str
    address: str
    city: str
    state: str
    zip: str

hospitals_data = [
    Hospital(id=1, name="Anytown General Hospital", address="123 Hospital Dr", city="Anytown", state="USA", zip="12345"),
    Hospital(id=2, name="Othertown Medical Center", address="456 Medical Dr", city="Othertown", state="USA", zip="67890"),
    # Add more hospital data here
]

@router.get("/", response_model=List[Hospital])
async def read_hospitals():
    return hospitals_data

@router.get("/{hospital_id}", response_model=Hospital)
async def read_hospital(hospital_id: int):
    hospital = next((h for h in hospitals_data if h.id == hospital_id), None)
    if hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@router.post("/", response_model=Hospital)
async def create_hospital(hospital: Hospital):
    hospitals_data.append(hospital)
    return hospital

@router.put("/{hospital_id}", response_model=Hospital)
async def update_hospital(hospital_id: int, hospital: Hospital):
    hospital_idx = next((i for i, h in enumerate(hospitals_data) if h.id == hospital_id), None)
    if hospital_idx is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospitals_data[hospital_idx] = hospital
    return hospital

@router.delete("/{hospital_id}")
async def delete_hospital(hospital_id: int):
    hospital_idx = next((i for i, h in enumerate(hospitals_data) if h.id == hospital_id), None)
    if hospital_idx is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    del hospitals_data[hospital_idx]
    return {"message": "Hospital deleted"}
