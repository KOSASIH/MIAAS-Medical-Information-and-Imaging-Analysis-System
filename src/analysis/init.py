from fastapi import FastAPI

app = FastAPI(title="Analysis API", description="API for analysis tasks", version="1.0.0")

from .image_analysis import image_analysis_router
from .data_analysis import data_analysis_router
from .predictive_model import predictive_model_router

app.include_router(image_analysis_router)
app.include_router(data_analysis_router)
app.include_router(predictive_model_router)
