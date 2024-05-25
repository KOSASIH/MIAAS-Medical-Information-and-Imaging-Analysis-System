import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2
from jose import jwt
from pydantic import BaseModel
from typing import List, Optional

from models.patient import Patient
from models.doctor import Doctor
from models.hospital import Hospital
from data import patients, doctors, hospitals

app = FastAPI(title="Medical Records API", description="API for managing medical records", version="1.0.0")

# CORS configuration
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Load data from files
patients_data = patients.load_patients()
doctors_data = doctors.load_doctors()
hospitals_data = hospitals.load_hospitals()

# Define API endpoints

@app.get("/patients/", response_class=JSONResponse)
async def read_patients():
    return patients_data

@app.get("/patients/{patient_id}", response_class=JSONResponse)
async def read_patient(patient_id: int):
    patient = next((p for p in patients_data if p.id == patient_id), None)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.post("/patients/", response_class=JSONResponse)
async def create_patient(patient: Patient):
    patients_data.append(patient)
    return patient

@app.put("/patients/{patient_id}", response_class=JSONResponse)
async def update_patient(patient_id: int, patient: Patient):
    patient_idx = next((i for i, p in enumerate(patients_data) if p.id == patient_id), None)
    if patient_idx is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    patients_data[patient_idx] = patient
    return patient

@app.delete("/patients/{patient_id}", response_class=JSONResponse)
async def delete_patient(patient_id: int):
    patient_idx = next((i for i, p in enumerate(patients_data) if p.id == patient_id), None)
    if patient_idx is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    del patients_data[patient_idx]
    return {"message": "Patient deleted"}

# Define API endpoints for doctors and hospitals
@app.get("/doctors/", response_class=JSONResponse)
async def read_doctors():
    return doctors_data

@app.get("/doctors/{doctor_id}", response_class=JSONResponse)
async def read_doctor(doctor_id: int):
    doctor = next((d for d in doctors_data if d.id == doctor_id), None)
    if doctor is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.post("/doctors/", response_class=JSONResponse)
async def create_doctor(doctor: Doctor):
    doctors_data.append(doctor)
    return doctor

@app.put("/doctors/{doctor_id}", response_class=JSONResponse)
async def update_doctor(doctor_id: int, doctor: Doctor):
    doctor_idx = next((i for i, d in enumerate(doctors_data) if d.id == doctor_id), None)
    if doctor_idx is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    doctors_data[doctor_idx] = doctor
    return doctor

@app.delete("/doctors/{doctor_id}", response_class=JSONResponse)
async def delete_doctor(doctor_id: int):
    doctor_idx = next((i for i, d in enumerate(doctors_data) if d.id == doctor_id), None)
    if doctor_idx is None:
        raise HTTPException(status_code=404, detail="Doctor not found")
    del doctors_data[doctor_idx]
    return {"message": "Doctor deleted"}

@app.get("/hospitals/", response_class=JSONResponse)
async def read_hospitals():
    return hospitals_data

@app.get("/hospitals/{hospital_id}", response_class=JSONResponse)
async def read_hospital(hospital_id: int):
    hospital = next((h for h in hospitals_data if h.id == hospital_id), None)
    if hospital is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    return hospital

@app.post("/hospitals/", response_class=JSONResponse)
async def create_hospital(hospital: Hospital):
    hospitals_data.append(hospital)
    return hospital

@app.put("/hospitals/{hospital_id}", response_class=JSONResponse)
async def update_hospital(hospital_id: int, hospital: Hospital):
    hospital_idx = next((i for i, h in enumerate(hospitals_data) if h.id == hospital_id), None)
    if hospital_idx is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    hospitals_data[hospital_idx] = hospital
    return hospital

@app.delete("/hospitals/{hospital_id}", response_class=JSONResponse)
async def delete_hospital(hospital_id: int):
    hospital_idx = next((i for i, h in enumerate(hospitals_data) if h.id == hospital_id), None)
    if hospital_idx is None:
        raise HTTPException(status_code=404, detail="Hospital not found")
    del hospitals_data[hospital_idx]
    return {"message": "Hospital deleted"}

# Define authentication endpoints
@app.post("/token")
async def login(request: Request):
    data = await request.json()
    if data.get("username") != "admin" or data.get("password") != "password":
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = jwt.encode({"sub": "admin"}, "secret", algorithm="HS256")
    return {"access_token": token}

# Define middleware
@app.middleware("http")
async def add_cors_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response

# Define static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define main function
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
