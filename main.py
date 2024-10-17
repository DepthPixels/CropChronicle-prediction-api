from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_interface import irrigation_data, predict_yield

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
  return {"message": "hey"}
  

@app.get("/predictions/")
def predictions(latitude: float, longitude: float, crop_type: str):
  irrigation = irrigation_data(latitude, longitude)
  predicted_yield = predict_yield(crop_type)
  
  return {"yield": predicted_yield,
          "irrigation": irrigation.tolist()}