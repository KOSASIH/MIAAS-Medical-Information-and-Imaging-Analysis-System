from fastapi import FastAPI

app = FastAPI(title="Medical Records API", description="API for managing medical records", version="1.0.0")

from .patient_api import patient_router
from .doctor_api import doctor_router
from .hospital_api import hospital_router

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(hospital_router)
