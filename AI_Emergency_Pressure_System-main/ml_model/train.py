import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
accidents = pd.read_csv("../data/accidents.csv")
ambulance = pd.read_csv("../data/ambulance_logs.csv")
weather = pd.read_csv("../data/weather.csv")
festivals = pd.read_csv("../data/festivals.csv")

# Merge datasets
df = accidents.merge(ambulance, on="date", how="left")
df = df.merge(weather, on="date", how="left")
df = df.merge(festivals, on="date", how="left")

# Handle missing values

# Festival: if no festival, set 0
df["festival"] = df["festival"].notnull().astype(int)

# Fill missing rainfall & temperature with 0
df["rainfall"] = df["rainfall"].fillna(0)
df["temperature"] = df["temperature"].fillna(df["temperature"].mean())

# Extract time features
df["date"] = pd.to_datetime(df["date"])
df["day"] = df["date"].dt.day
df["month"] = df["date"].dt.month

# Encode location
df["location"] = df["location"].astype("category").cat.codes

# Select features
X = df[[
    "accident_count",
    "rainfall",
    "temperature",
    "festival",
    "day",
    "month",
    "location"
]]

y = df["ambulance_arrivals"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

print("✅ Model trained successfully and saved as model.pkl")
