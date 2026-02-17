from fastapi import FastAPI
from pydantic import BaseModel
from ml_model.predict import predict_pressure
from utils.alert_engine import generate_alert

app = FastAPI()

class InputData(BaseModel):
    accident_count: int
    rainfall: float
    temperature: float
    festival: int
    day: int
    month: int
    location: int

@app.post("/predict")
def predict(data: InputData):

    # Validation
    if data.day < 1 or data.day > 31:
        return {"error": "Invalid day"}

    prediction = predict_pressure(data.dict())
    alert = generate_alert(prediction)

    return {
        "predicted_load": prediction,
        "alert_status": alert
    }
