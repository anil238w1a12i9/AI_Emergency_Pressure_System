import pandas as pd

def load_data():
    accidents = pd.read_csv("data/accidents.csv")
    ambulance = pd.read_csv("data/ambulance_logs.csv")
    weather = pd.read_csv("data/weather.csv")
    festivals = pd.read_csv("data/festivals.csv")
    return accidents, ambulance, weather, festivals
