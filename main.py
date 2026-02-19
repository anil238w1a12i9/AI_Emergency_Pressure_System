from services.data_loader import load_data
from models.pressure_predictor import predict_pressure
from alerts.alert_engine import generate_alert

import sys

def main():
    try:
        accidents, ambulance, weather, festivals = load_data()

        predicted_load = predict_pressure(accidents, ambulance)

        alerts = generate_alert(predicted_load)

        print("\n📊 Emergency Load Prediction Results\n")
        print("-" * 40)

        for i in range(len(alerts)):
            print(f"Day {i+1}: {alerts[i]}")

        print("\n✔ System executed successfully.\n")

    except FileNotFoundError as e:
        print("❌ Required data file missing.")
        print("Details:", e)

    except ValueError as e:
        print("❌ Data processing error.")
        print("Details:", e)

    except Exception as e:
        print("❌ Unexpected system error.")
        print("Details:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
