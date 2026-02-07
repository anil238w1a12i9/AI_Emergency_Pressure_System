from services.data_loader import load_data
from models.pressure_predictor import predict_pressure
from alerts.alert_engine import generate_alert

try:
    # Step 1: Load all datasets
    accidents, ambulance, weather, festivals = load_data()

    # Step 2: Predict emergency / ambulance load
    predicted_load = predict_pressure(accidents, ambulance)

    # Step 3: Generate alerts based on predicted load
    alerts = generate_alert(predicted_load)

    # Step 4: Display results
    for i in range(len(alerts)):
        print(f"Day {i+1}: {alerts[i]}")

except FileNotFoundError as e:
    print("❌ Data file not found. Please check CSV files.")
    print("Details:", e)

except ValueError as e:
    print("❌ Data mismatch error. Please ensure datasets have equal rows.")
    print("Details:", e)

except Exception as e:
    print("❌ Unexpected system error occurred.")
    print("Details:", e)
