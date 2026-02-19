import os
import pandas as pd
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    try:
        base_path = os.path.dirname(os.path.dirname(__file__))
        data_path = os.path.join(base_path, "data")

        required_files = [
            "accidents.csv",
            "ambulance_logs.csv",
            "weather.csv",
            "festivals.csv"
        ]

        for file in required_files:
            if not os.path.exists(os.path.join(data_path, file)):
                raise FileNotFoundError(f"{file} not found in data folder")

        accidents = pd.read_csv(os.path.join(data_path, "accidents.csv"))
        ambulance = pd.read_csv(os.path.join(data_path, "ambulance_logs.csv"))
        weather = pd.read_csv(os.path.join(data_path, "weather.csv"))
        festivals = pd.read_csv(os.path.join(data_path, "festivals.csv"))

        logging.info("All datasets loaded successfully.")
        return accidents, ambulance, weather, festivals

    except Exception as e:
        logging.error(f"Error loading data: {str(e)}")
        raise
