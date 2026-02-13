import joblib
import pandas as pd

import os

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model.pkl")

model = joblib.load(model_path)


def predict_pressure(input_dict):
    df = pd.DataFrame([input_dict])
    prediction = model.predict(df)
    return float(prediction[0])
