from fastapi import FastAPI
from model_interface import irrigation_data, predict_yield

app = FastAPI()


@app.get("/predictions/")
def predictions(latitude: float, longitude: float, crop_type: str):
  irrigation = irrigation_data(latitude, longitude)
  predicted_yield = predict_yield(crop_type)
  
  return {"yield": predicted_yield,
          "irrigation": irrigation.tolist()}