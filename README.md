Project Title:
AI Emergency Pressure & Ambulance Load Prediction System

Phase:
Phase 1 – Core Foundation

Objective:
Predict emergency department overload using historical accident,
ambulance, weather and festival data.

Technologies Used:
- Python
- Pandas
- Scikit-learn


Features Implemented:
- Emergency pressure prediction
- Ambulance load estimation
- Alert generation (High/Moderate/Normal)

Future Scope:
- Real-time data
- Deep learning
- Hospital dashboards




PHASE 2:




# AI Emergency Pressure & Ambulance Load Prediction System

## Phase 2 – Logic Expansion & Enhancements

### Project Objective
To predict ambulance load and emergency pressure using accident,
weather, festival and time-series data with real-time alert generation.

---

## Architecture

Frontend (HTML + Chart.js)
↓
Backend API (FastAPI)
↓
ML Model (Linear Regression - Saved as model.pkl)
↓
CSV Data Sources



---

## Features Implemented

✔ Modular architecture (ML / Backend / Frontend separated)  
✔ Geospatial modeling (Zone-based encoding)  
✔ Time-series modeling (Day & Month extraction)  
✔ Weather integration  
✔ Festival impact modeling  
✔ Real-time alert threshold system  
✔ API-based prediction endpoint  
✔ Interactive dashboard with visualization  

---

## API Endpoint

POST `/predict`

Example JSON:

```json
{
  "accident_count": 12,
  "rainfall": 5,
  "temperature": 30,
  "festival": 0,
  "day": 5,
  "month": 1,
  "location": 0
}





How To Run

Train model:

python ml_model/train.py


Start API:

uvicorn backend.app:app --reload


Open:

http://127.0.0.1:8000/docs


Open dashboard:

frontend/dashboard.html

##Phase 3##
# AI Emergency Pressure & Ambulance Load Prediction System

## Overview
This system predicts emergency pressure and ambulance load using historical accident data.

## Features
- Multi-dataset integration
- Alert classification system
- Secure file validation
- Logging system
- Production-ready structure

## Project Structure
- services/ → Data loading
- models/ → Prediction logic
- alerts/ → Alert generation
- data/ → CSV datasets
- frontend/ → Dashboard UI

## How to Run

1. Install requirements:
   pip install pandas

2. Run:
   python main.py

## Security Improvements
- File validation
- Error logging
- Exception handling

## Future Scope
- Real-time API integration
- Deployment on cloud
- Advanced ML model integration

